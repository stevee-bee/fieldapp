
# A database-backed Flask website to track and manage field crops.
# based on reference article: https://blog.pythonanywhere.com/121/
# and Miguel's Microblog Mega-Tutorial: https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world
# modified for DSE

# external packages
from flask import Flask
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

# not used from Miguel's Microblog Mega-Tutorial
# from flask_babel import Babel, lazy_gettext as _l
# from flask_mail import Mail
# from flask_moment import Moment

# internal modules
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)
login.login_view = 'login'
# mail = Mail(app)
bootstrap = Bootstrap(app)
# moment = Moment(app)
# babel = Babel(app)

import routes, models, errors


###################
### decorators  ###
###################

# @app.shell_context_processor
# def make_shell_context():
#     return {'db': db, 'User': User, 'Field': Field, 'Seed': Seed}

