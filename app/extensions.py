from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from app.config import Config
from flask_bcrypt import Bcrypt
import os

app = Flask(__name__)
app.config.from_object(Config)

bcrypt = Bcrypt(app)

db = SQLAlchemy(app)



###########################
# Authentication
###########################

# TODO: Add authentication setup code here!



