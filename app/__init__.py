from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.config import Config
import os
from flask_login import LoginManager


app = Flask(__name__)
app.config.from_object(Config)
app.secret_key = os.environ.get('SECRET_KEY')

db = SQLAlchemy(app)

from app.controllers.main import main
from app.controllers.movies import movies
from app.controllers.tags import tags
from app.controllers.auth import auth

app.register_blueprint(main)
app.register_blueprint(movies)
app.register_blueprint(tags)
app.register_blueprint(auth)

login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.init_app(app)

from .models import User

@login_manager.user_loader
def load_user(user_id):
  return User.query.get(int(user_id))

with app.app_context():
  db.create_all()


