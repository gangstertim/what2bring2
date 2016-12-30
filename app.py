from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for

app = Flask(__name__)

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
