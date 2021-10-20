from flask import flash, redirect, render_template, request, url_for
from flask_login import current_user, login_required, login_user, logout_user
from werkzeug.urls import url_parse

from flask_app import app, db
from forms import LoginForm, RegistrationForm, FieldForm, SeedForm
from models import User, Field, Seed


@app.route('/')
@app.route('/index')
@login_required
def index():
    return render_template('index.html', fields=Field.query.all())

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)

@app.route('/addfield', methods=['GET', 'POST'])
@login_required
def addfield():
    form = FieldForm()
    if form.validate_on_submit():
        field = Field(
            number = form.number.data,
            name = form.name.data,
            land_loc = form.land_loc.data,
            comment = form.comment.data
        )
        db.session.add(field)
        db.session.commit()
        flash('New field #{} "{}" successfully added.'.format(form.number.data, form.name.data))
        return redirect(url_for('index'))
    return render_template('addfield.html', form=form)

@app.route('/editfield/<n>', methods=['GET', 'POST'])
@login_required
def editfield(n):
    field = Field.query.get(n)
    form = FieldForm()
    if form.validate_on_submit():
        field.name = form.name.data
        field.land_loc = form.land_loc.data
        field.comment = form.comment.data
        db.session.commit()
        flash('Field #{} "{}" successfully updated.'.format(form.number.data, form.name.data))
        return redirect(url_for('index'))
    elif request.method == 'GET':
        form.name.data = field.name
        form.land_loc.data = field.land_loc
        form.comment.data = field.comment
    return render_template('editfield.html', form=form, field=field)

@app.route('/addseed/<n>', methods=['GET', 'POST'])
@login_required
def addseed(n):
    field = Field.query.get(n)
    form = SeedForm()
    if form.validate_on_submit():
        seed = Seed(
            date_seeded = form.date_seeded.data,
            name = form.name.data,
            comment = form.comment.data,
            field = field
        )
        db.session.add(seed)
        db.session.commit()
    seeds = Seed.query.filter_by(field_id=field.id).order_by(Seed.date_seeded.desc())
    return render_template('addseed.html', form=form, field=field, seeds=seeds)

