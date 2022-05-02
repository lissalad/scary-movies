from sqlite3 import Date
from tkinter import N
from tkinter.tix import Select
from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, DateField, SelectField, SubmitField
from wtforms.ext.sqlalchemy.fields import QuerySelectField, QuerySelectMultipleField
from wtforms.validators import DataRequired, Length, URL
from app.models import Movie, Tag
from flask_login import current_user


class MovieForm(FlaskForm):
  title = StringField('Title')
  release_year = StringField('Release Year)')

  tags = QuerySelectMultipleField('Tags',
    query_factory=lambda: Tag.query.filter_by(user_id=current_user.id), get_label='name')

  submit = SubmitField('Submit')

class TagForm(FlaskForm):
  name = StringField('Name',validators=[DataRequired(),Length(min=1)])
  submit = SubmitField('Submit')

