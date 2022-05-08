from app import db
from sqlalchemy.orm import backref
from flask_login import UserMixin

class Movie(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.String(255), nullable=False)
  release_year = db.Column(db.String(4))
  img_url = db.Column(db.String(255), nullable=False)

  last_watched = db.Column(db.Date)
  director = db.Column(db.String(255))
  budget = db.Column(db.Integer)
  box_office = db.Column(db.Integer)

  user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

  user = db.relationship('User', back_populates='movies')
  tags = db.relationship('Tag', secondary='movie_tags', back_populates='movies')

class Tag(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(255), nullable=False)
  user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

  user = db.relationship('User', back_populates='tags')
  movies = db.relationship('Movie', secondary='movie_tags', back_populates='tags')

movie_tags_table = db.Table('movie_tags',
  db.Column('movie_id', db.Integer, db.ForeignKey('movie.id'), primary_key=True),
  db.Column('tag_id', db.Integer, db.ForeignKey('tag.id'), primary_key=True)
)

class User(db.Model, UserMixin):
  id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
  email = db.Column(db.String(100), unique=True)
  password = db.Column(db.String(100))
  name = db.Column(db.String(1000))

  movies = db.relationship('Movie', back_populates='user')
  tags = db.relationship('Tag', back_populates='user')



