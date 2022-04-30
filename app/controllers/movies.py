from flask import Blueprint, request, render_template, redirect, url_for, flash
from app.forms.main import MovieForm, TagForm
from app.models import Movie, Tag
from app import app, db
from flask_login import login_required

movies = Blueprint('movies', __name__)

@movies.route('/movies')
@login_required
def index():
  movies = Movie.query.all()
  return render_template('movies/index.html', movies=movies)

@movies.route('/movies/new', methods=['GET', 'POST'])
@login_required
def new():
    form = MovieForm()

    if form.validate_on_submit(): 
      new_movie = Movie(
        title=form.title.data,
        release_year=form.release_year.data,
        tags=form.tags.data,
      )
      db.session.add(new_movie)
      db.session.commit()

      flash('new movie created')
      return redirect(url_for('movies.show', id=new_movie.id))
    return render_template('movies/new.html', form=form)

@movies.route('/movies/<id>', methods=['GET'])
@login_required
def show(id):
  movie = Movie.query.get(id)
  return render_template('movies/show.html', movie=movie)

@movies.route('/movies/<id>/edit', methods=['GET', 'POST'])
@login_required
def edit(id):
  movie=Movie.query.get(id)
  form = MovieForm(obj=movie)

  if request.method == 'POST':
    movie.title = form.title.data
    movie.release_year = form.release_year.data
    movie.tags = form.tags.data

    db.session.add(movie)
    db.session.commit()

    flash('movie updated')
    return redirect(url_for('movies.show', form=form, id=movie.id))
  return render_template('movies/edit.html', form=form, movie=movie)

@movies.route('/movies/<id>/delete')
@login_required
def delete(id):
  movie = Movie.query.get(id)
  db.session.delete(movie)
  db.session.commit()

  return redirect(url_for('movies.index'))