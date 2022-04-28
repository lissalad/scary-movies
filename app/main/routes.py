from flask import Blueprint, request, render_template, redirect, url_for, flash
from app.main.forms import MovieForm, TagForm
from app.models import Movie, Tag
from app.extensions import app, bcrypt, db

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return render_template('index.html')

@main.route('/tags')
def tags():
  tags = Tag.query.all()
  return render_template('tags.html', tags=tags)

@main.route('/movie/new', methods=['GET', 'POST'])
# @login_required
def new_movie():
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
      # return redirect(url_for('main.book_detail', book_id=new_book.id))
    return render_template('new_movie.html', form=form)

@main.route('/tag/new', methods=['GET', 'POST'])
# @login_required
def new_tag():

    form = TagForm()

    if form.validate_on_submit(): 
      new_tag = Tag(name=form.name.data)
      db.session.add(new_tag)
      db.session.commit()

      flash('new tag created')
      print("hi")
      return redirect(url_for('main.tags'))

    return render_template('new_tag.html', form=form)

@main.route('/tag/<tag_id>', methods=['GET'])
# @login_required
def tag_detail(tag_id):
  tag = Tag.query.get(tag_id)

  return render_template('tag_detail.html', tag=tag)

@main.route('/tag/<tag_id>/edit', methods=['GET', 'POST'])
# @login_required
def edit_tag(tag_id):

  tag = Tag.query.get(tag_id)
  form = TagForm(obj=tag)

  if request.method == 'POST':
    tag = Tag(name=form.name.data)
    db.session.add(tag)
    db.session.commit()

    flash('tag updated')
    return redirect(url_for('main.tag_detail', form=form, tag_id=tag.id))

  tag = Tag.query.get(tag_id)
  return render_template('edit_tag.html', form=form, tag=tag)