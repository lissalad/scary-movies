from flask import Blueprint, request, render_template, redirect, url_for, flash
from app.forms.main import MovieForm, TagForm
from app.models import Movie, Tag
from app import app, db
from flask_login import login_required, current_user

movies = Blueprint('movies', __name__)

@movies.route('/movies')
@login_required
def index():
  movies = Movie.query.filter_by(user_id=current_user.id)
  return render_template('movies/index.html', movies=movies)

@movies.route('/movies/new', methods=['GET', 'POST'])
@login_required
def new():
    form = MovieForm()
    isEmpty = True
    if len(current_user.tags) > 0:
      isEmpty = False
      print("not empty!")

    if request.method == 'POST':
      new_movie = Movie(
        title=form.title.data,
        release_year=form.release_year.data,
        img_url=form.img_url.data,
        tags=form.tags.data,
        user_id=current_user.id,
      )
      db.session.add(new_movie)
      db.session.commit()
      
      flash('new movie created')
      return redirect(url_for('movies.show', id=new_movie.id))
    # flash('failed to create movie')
    return render_template('movies/new.html', form=form, isEmpty=isEmpty)

@movies.route('/movies/<id>', methods=['GET'])
@login_required
def show(id):
  movie = Movie.query.get(id)
  if movie in current_user.movies:
    return render_template('movies/show.html', movie=movie)
  else:
    flash('that is not yours')
    return redirect(url_for('movies.index'))

@movies.route('/movies/<id>/edit', methods=['GET', 'POST'])
@login_required
def edit(id):
  movie=Movie.query.get(id)
  if movie in current_user.movies:
    form = MovieForm(obj=movie)

    isEmpty = True
    if len(current_user.tags) > 0:
      isEmpty = False

    if request.method == 'POST':
      movie.title = form.title.data
      movie.release_year = form.release_year.data
      img_url=form.img_url.data,
      movie.tags = form.tags.data

      print(form.tags)

      db.session.add(movie)
      db.session.commit()


      flash('movie updated')
      return redirect(url_for('movies.show', form=form, id=movie.id))
    # flash('failed to update movie')
    return render_template('movies/edit.html', form=form, movie=movie, isEmpty=isEmpty)
  else:
    flash('that is not yours')
    return redirect(url_for('movies.index'))

@movies.route('/movies/<id>/delete')
@login_required
def delete(id):
  movie = Movie.query.get(id)

  if movie in current_user.movies:
    db.session.delete(movie)
    db.session.commit()
    flash('movie deleted')
    return redirect(url_for('movies.index'))

  else:
    flash('that is not yours')
    return redirect(url_for('movies.index'))
