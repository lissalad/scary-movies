from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.config import Config
import os

app = Flask(__name__)
app.config.from_object(Config)
app.secret_key = os.environ.get('SECRET_KEY')

db = SQLAlchemy(app)

from app.controllers.main import main
from app.controllers.movies import movies
from app.controllers.tags import tags


app.register_blueprint(main)
app.register_blueprint(movies)
app.register_blueprint(tags)


with app.app_context():
  db.create_all()


