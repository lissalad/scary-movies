from flask import Blueprint, request, render_template, redirect, url_for, flash
from app.forms.main import MovieForm, TagForm
from app.models import Movie, Tag
from app import app, db

movies = Blueprint('movies', __name__)

@movies.route('/movies/new', methods=['GET', 'POST'])
# @login_required
def new():
    form = MovieForm()

    if form.validate_on_submit(): 
      new_movie = Movie(
        title=form.title.data,
        release_date=form.release_date.data,
        tags=form.tags.data,
      )
      db.session.add(new_movie)
      db.session.commit()

      flash('new movie created')
      return redirect(url_for('movies.show', id=new_movie.id))
    return render_template('movies/new.html', form=form)

@movies.route('/movies/<id>', methods=['GET'])
# @login_required
def show(id):
  movie = Movie.query.get(id)
  return render_template('movies/show.html', movie=movie)