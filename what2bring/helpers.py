from flask import g
import sqlite3

def connect_db():
    rv = sqlite3.connect(g.DATABASE_CONFIG)
    rv.row_factory = sqlite3.Row
    return rv

def get_db():
    # Opens a new database connection if there is none for app context
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db
