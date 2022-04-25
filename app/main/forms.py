from tkinter.tix import Select
from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, DateField, SelectField, SubmitField
from wtforms.ext.sqlalchemy.fields import QuerySelectField, QuerySelectMultipleField
from wtforms.validators import DataRequired, Length, URL
from app.models import Movie, Tags


class MovieForm(FlaskForm):

  title = StringField('Title')
  release_date = DateField()
  tags = SelectField('Tags', choices=Tags.choices())

  submit = SubmitField('Submit')