from flask import Blueprint, request, render_template, redirect, url_for, flash
from app.forms.main import MovieForm, TagForm
from app.models import Movie, Tag
from app import app, db

main = Blueprint('main', __name__)

@main.route('/')
def index():
  return render_template('index.html')
  

