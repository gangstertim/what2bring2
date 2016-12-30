from flask import Flask, render_template, request, redirect, url_for
import sqlite3
import os

# create the application

app = Flask(__name__)

# Load default config
app.config.update(dict(
    DATABASE=os.path.join(app.root_path, 'what2bring.db'),
    DEBUG=True,
    SECRET_KEY='dev key',
    USERNAME='admin',
    PASSWORD='default'
))

# Allow default config to be overridden by environmental variables
app.config.from_envvar('WHAT2BRING_SETTINGS', silent=True)




def connect_db():
    rv = sqlite3.connect(app.config['DATABASE'])
    rv.row_factory = sqlite3.Row
    return rv


@app.route('/')
def hello_world():
    return render_template('home.html')

@app.route('/about')
def show_about():
    return render_template('about.html')

@app.route('/events/<int:event_no>')
def show_event(event_no):
    return render_template('event.html', event_no=event_no)

@app.route('/events', methods=['POST'])
def create_event():
    event_no=100 #TODO
    print request.form
    return redirect(url_for('show_event', event_no=event_no))
