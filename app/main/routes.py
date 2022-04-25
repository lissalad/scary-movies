from flask import Blueprint, request, render_template, redirect, url_for, flash
from app.main.forms import MovieForm
from app.models import Movie
from app.extensions import app, bcrypt, db


main = Blueprint('main', __name__)

@main.route('/')
def home():
    return render_template('index.html')

@main.route('/new_movie', methods=['GET', 'POST'])
# @login_required
def new_movie():
    form = MovieForm()

    if form.validate_on_submit(): 
      new_movie = Movie(
      title=form.title.data,
      release_data=form.release_date.data,
      tags=form.tags.data,
      )
      db.session.add(new_movie)
      db.session.commit()

      flash('new movie created')
      # return redirect(url_for('main.book_detail', book_id=new_book.id))
    return render_template('index.html')