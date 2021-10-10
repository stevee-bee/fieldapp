
# A database-backed Flask website to track and manage field crops.
# based on reference article: https://blog.pythonanywhere.com/121/
# modified for DSE

# external packages
from datetime import datetime
from flask import flash, Flask, redirect, render_template, request, url_for
from flask_login import current_user, login_required, login_user, LoginManager, logout_user, UserMixin
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import check_password_hash

# internal packages
from config import Config
from forms import LoginForm

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)



###################
###   models    ###
###################

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return '<User {}>'.format(self.username)


class Field(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.Integer, index=True, unique=True)
    name = db.Column(db.String(32))
    land_loc = db.Column(db.String(32))
    comment = db.Column(db.String(255))
    seeds = db.relationship('Seed', backref='field', lazy='dynamic')

    def __repr__(self):
        return '<Field {} "{}">'.format(self.number, self.name)


class Seed(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32))
    date_seeded = db.Column(db.Date, default=datetime.utcnow)
    date_harvested = db.Column(db.Date)
    bu_yield = db.Column(db.Numeric(4,1))
    comment = db.Column(db.String(255))
    field_id = db.Column(db.Integer, db.ForeignKey('field.id'))

    def __repr__(self):
        return '<Seed {}>'.format(self.name)



###################
### decorators  ###
###################

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Field': Field, 'Seed': Seed}



###################
###    views    ###
###################

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Dana', 'email': 'dbschindel@hotmail.com'}
    fields = [
        {
            'number': 1,
            'name': 'Unger',
            'land_loc': 'SW 24-18-11'
        },
        {
            'number': 2,
            'name': 'Home West',
            'land_loc': 'NW 13-18-11'
        },
        {
            'number': 3,
            'name': 'Home Half',
            'land_loc': 'NE 13-18-11'
        }
    ]
    return render_template('index.html', user=user, fields=fields)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', form=form)
