from flask import Blueprint, request, render_template, redirect, url_for, flash
from app.forms.main import MovieForm, TagForm
from app.models import Movie, Tag
from app import app, db

tags = Blueprint('tags', __name__)

@tags.route('/tags')
def index():
  tags = Tag.query.all()
  return render_template('tags/index.html', tags=tags)

@tags.route('/tags/new', methods=['GET', 'POST'])
# @login_required
def new():
    form = TagForm()

    if form.validate_on_submit(): 
      new_tag = Tag(name=form.name.data)
      db.session.add(new_tag)
      db.session.commit()

      flash('new tag created')
      print("hi")
      return redirect(url_for('tags.index'))

    return render_template('tags/new.html', form=form)

@tags.route('/tags/<id>', methods=['GET'])
# @login_required
def show(id):
  tag = Tag.query.get(id)
  return render_template('tags/show.html', tag=tag)

@tags.route('/tags/<id>/edit', methods=['GET', 'POST'])
# @login_required
def edit(id):

  tag = Tag.query.get(id)
  form = TagForm(obj=tag)

  if request.method == 'POST':
    tag.name = form.name.data
    db.session.add(tag)
    db.session.commit()

    flash('tag updated')
    return redirect(url_for('tags.show', form=form, id=tag.id))

  return render_template('tags/edit.html', form=form, tag=tag)
  
