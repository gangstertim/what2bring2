from flask import render_template
from . import routes

@routes.route('/')
def show_home():
    return render_template('home.html')

@routes.route('/about')
def show_about():
    return render_template('about.html')


