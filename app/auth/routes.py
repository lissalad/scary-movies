from flask import Blueprint, request, render_template, redirect, url_for, flash

auth = Blueprint('auth', __name__)

@auth.route('/')
def home():
    return render_template('index.html')

@auth.route('/new_movie')
def new_movie():
    return render_template('new_movie.html')