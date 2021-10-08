
# A database-backed Flask website to track and manage field crops.
# based on reference article: https://blog.pythonanywhere.com/121/
# modified for DSE

from datetime import datetime
from flask import Flask, redirect, render_template, request, url_for
from flask_login import current_user, login_required, login_user, LoginManager, logout_user, UserMixin
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import check_password_hash

app = Flask(__name__)
app.config["DEBUG"] = True

SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://{username}:{password}@{hostname}/{databasename}".format(
    username="dse",
    password="Ap4tW!veyHp35nM5",
    hostname="dse.mysql.pythonanywhere-services.com",
    databasename="dse$fma",
)
app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
app.config["SQLALCHEMY_POOL_RECYCLE"] = 299
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)
# migrate = Migrate(app, db)


@app.route('/')
def hello_world():
    return 'Hello from Flask!'

