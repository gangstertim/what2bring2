from flask import render_template, redirect, request, url_for, flash
from ..helpers import get_db
from . import routes

@routes.route('/events/<int:event_no>/guest', methods=['POST'])
def create_guest(event_no):
    #TODO
    return

@routes.route('/events/<int:event_no>')
def show_event(event_no):
    db = get_db()
    q = db.execute("""select
        eventName,
        eventLocation,
        eventDescription,
        eventDatetime,
        hostName,
        dishesToBring,
        acceptCash,
        cashAmount
    from events where id = ?""", [event_no])
    event = q.fetchone()

    if (event is None):
        return "event not found!" #TODO clean this up    
    
    return render_template('event.html', event=event)

@routes.route('/events', methods=['POST', 'GET'])
def handle_event():
    db = get_db()
    if request.method == 'POST':
        return create_event(db, request.form)
    elif request.method == 'GET':
        return show_events(db)

def show_events(db):
    q = db.execute("""select 
        id,
        eventName, 
        eventLocation,
        eventDescription,
        eventDatetime,
        hostName,
        hostEmail,
        dishesToBring,
        acceptCash,
        cashAmount
    from events order by id desc""")
    events = q.fetchall()
    return render_template('events.html', events=events)


def create_event(db, form):
    eventDatetime = 0 #TODO convert event date & time into epoch datetime
    acceptCash = 1 if form['acceptCash'] else 0
    db.execute("""insert into events (
        eventName, 
        eventLocation,
        eventDescription,
        eventDatetime,
        hostName,
        hostEmail,
        dishesToBring,
        acceptCash,
        cashAmount,
        created_at,
        updated_at
    ) values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""", [
        form['eventName'], 
        form['eventLocation'],
        form['eventDescription'],
        eventDatetime,
        form['hostName'],
        form['hostEmail'],
        form['dishesToBring'],
        acceptCash,
        form['cashAmount'],
        "DATETIME('now')",
        "DATETIME('now')"
    ])
    db.commit()
    flash('New entry was successfully posted')
    return redirect(url_for('routes.show_event', event_no=1)) #TODO get autoincremented event number

