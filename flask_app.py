
# A database-backed Flask website to track and manage field crops.
# based on reference article: https://blog.pythonanywhere.com/121/
# modified for DSE

# external packages
from flask import Flask
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

# internal modules
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
bootstrap = Bootstrap(app)
login = LoginManager(app)
login.login_view = 'login'

db = SQLAlchemy(app)
migrate = Migrate(app, db)

import routes, models, errors


###################
### decorators  ###
###################

# @app.shell_context_processor
# def make_shell_context():
#     return {'db': db, 'User': User, 'Field': Field, 'Seed': Seed}

