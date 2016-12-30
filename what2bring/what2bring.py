from flask import Flask, render_template, request, redirect, url_for, g, flash
import sqlite3
import os

# create the application
app = Flask(__name__)

# Load default config, allow override by environmental variabldes
app.config.update(dict(
    DATABASE=os.path.join(app.root_path, 'what2bring.db'),
    DEBUG=True,
    SECRET_KEY='dev key',
    USERNAME='admin',
    PASSWORD='default'
))
app.config.from_envvar('WHAT2BRING_SETTINGS', silent=True)


#Establish DB initialization, connection, & teardown methods
def connect_db():
    rv = sqlite3.connect(app.config['DATABASE'])
    rv.row_factory = sqlite3.Row
    return rv

def init_db():
    db = get_db()
    with app.open_resource('schema.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()

def get_db():
    # Opens a new database connection if there is none for app context
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db

@app.cli.command('initdb')
def initdb_command():
    init_db()
    print('Initialized the database')

@app.teardown_appcontext
def close_db(error):
    # Closes the database again at the end of the request.
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()



# ROUTES
@app.route('/')
def hello_world():
    return render_template('home.html')

@app.route('/about')
def show_about():
    return render_template('about.html')

@app.route('/events/<int:event_no>')
def show_event(event_no):
    return render_template('event.html', event_no=event_no)

@app.route('/events', methods=['POST', 'GET'])
def create_event():
    db = get_db()
    if request.method == 'POST':
        db.execute('insert into events (eventName, hostName) values (?, ?)',
            [request.form['eventName'], request.form['hostName']])
        db.commit()
        flash('New entry was successfully posted')
        return redirect(url_for('show_event', event_no=100)) #TODO
    elif request.method == 'GET':
        cur = db.execute('select eventName, hostName from events order by id desc')
        events = cur.fetchall()
        print events
        return render_template('events.html', events=events)
