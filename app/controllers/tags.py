from flask import Blueprint, request, render_template, redirect, url_for, flash
from app.forms.main import MovieForm, TagForm
from app.models import Movie, Tag
from app import app, db
from flask_login import login_required, current_user

tags = Blueprint('tags', __name__)

@tags.route('/tags')
@login_required
def index():
  tags = Tag.query.filter_by(user_id=current_user.id)
  return render_template('tags/index.html', tags=tags)

@tags.route('/tags/new', methods=['GET', 'POST'])
@login_required
def new():
    form = TagForm()

    if form.validate_on_submit(): 
      new_tag = Tag(
        name=form.name.data, 
        user_id=current_user.id,
      )

      db.session.add(new_tag)
      db.session.commit()
      flash('new tag created')
      print("hi")
      return redirect(url_for('tags.index'))

    return render_template('tags/new.html', form=form)

@tags.route('/tags/<id>', methods=['GET'])
@login_required
def show(id):
  tag = Tag.query.get(id)
  if tag in current_user.tags:
    return render_template('tags/show.html', tag=tag)
  else:
    flash('that is not yours')
    return redirect(url_for('tags.index'))

@tags.route('/tags/<id>/edit', methods=['GET', 'POST'])
@login_required
def edit(id):

  tag = Tag.query.get(id)
  if tag in current_user.tags:
    form = TagForm(obj=tag)

    if request.method == 'POST':
      tag.name = form.name.data
      db.session.add(tag)
      db.session.commit()

      flash('tag updated')
      return redirect(url_for('tags.show', form=form, id=tag.id))
    return render_template('tags/edit.html', form=form, tag=tag)
  else:
    flash('that is not yours')
    return redirect(url_for('tags.index'))
  
@tags.route('/tags/<id>/delete')
@login_required
def delete(id):
  tag = Tag.query.get(id)
  if tag in current_user.tags:
    db.session.delete(tag) 
    db.session.commit()
    return redirect(url_for('tags.index'))
  else:
    flash('that is not yours')
    return redirect(url_for('tags.index'))
