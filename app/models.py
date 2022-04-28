from app import db
from sqlalchemy.orm import backref
from flask_login import UserMixin

class Movie(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.String(255), nullable=False)
  release_date = db.Column(db.String(4))

  tags = db.relationship('Tag', secondary='movie_tags', back_populates='movies')

class Tag(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(255), nullable=False)

  movies = db.relationship('Movie', secondary='movie_tags', back_populates='tags')

movie_tags_table = db.Table('movie_tags',
    db.Column('movie_id', db.Integer, db.ForeignKey('movie.id'), primary_key=True),
    db.Column('tag_id', db.Integer, db.ForeignKey('tag.id'), primary_key=True)
)


