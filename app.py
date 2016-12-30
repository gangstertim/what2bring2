from flask import Flask
from flask import render_template

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




