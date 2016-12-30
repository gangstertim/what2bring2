from flask import Flask, g
from helpers import get_db 
from routes import *
import os

# Load default config, allow override by environmental variabldes
app = Flask(__name__)
app.config.update(dict(
    DATABASE=os.path.join(app.root_path, 'what2bring.db'),
    DEBUG=True,
    SECRET_KEY='dev key',
    USERNAME='admin',
    PASSWORD='default'
))
app.config.from_envvar('WHAT2BRING_SETTINGS', silent=True)

# register routes
app.register_blueprint(routes)

def init_db():
    db = get_db()
    with app.open_resource('schema.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()

@app.cli.command('initdb')
def initdb_command():
    g.DATABASE_CONFIG = app.config['DATABASE'];
    init_db()
    print('Initialized the database')

@app.teardown_appcontext
def close_db(error):
    # Closes the database again at the end of the request.
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()

