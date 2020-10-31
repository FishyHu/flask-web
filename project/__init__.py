from flask import *
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
import os

app = Flask(__name__)
app.config.from_object(os.environ['SETTINGS'])

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

from project.home.views import home_blueprint
from project.users.views import users_blueprint
app.register_blueprint(home_blueprint)
app.register_blueprint(users_blueprint)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'users.login'

from .database import writer

@login_manager.user_loader
def check_it(user_id):
	return writer.query.filter(writer.id==int(user_id)).first()