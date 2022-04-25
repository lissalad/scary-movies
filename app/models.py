from app import db
from sqlalchemy.orm import backref
from flask_login import UserMixin
import enum

class FormEnum(enum.Enum):
    """Helper class to make it easier to use enums with forms."""
    @classmethod
    def choices(cls):
        return [(choice.name, choice) for choice in cls]

    def __str__(self):
        return str(self.value)

class Tags(enum.Enum):
    ALIEN = 'Alien'
    SLASHER = 'Slasher'
    PARANORMAL = 'Paranormal'
    PSYCHOLOGICAL = 'Psychological'

class Movie(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.String(80), nullable=False)
  release_date = db.Column(db.Date)

  tags = db.relationship('Tag', secondary='movie_tags', back_populates='movies')

# class Tag(db.Model):
#   id = db.Column(db.Integer, primary_key=True)
#   name = db.Column(db.String(80), nullable=False)

#   movies = db.relationship('Movie', secondary='movie_tags', back_populates='tags')




