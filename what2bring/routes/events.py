from flask import render_template, redirect, request, url_for, flash
from ..helpers import get_db
from . import routes

@routes.route('/events/<int:id>/guest', methods=['POST'])
def create_guest(id):
    db = get_db()
    db.execute("""insert into guests (
        name,
        email,
        dishes,
        bringing_cash,
        event_id,
        created_at
    ) values (?, ?, ?, ?, ?, ?)""", [
        request.form['name'],
        request.form['email'],
        request.form['dishes'],
        request.form['bringing_cash'],
        id,
        "DATETIME('now')"
    ])
    db.commit()
    flash("Guest successfully added!")
    #TODO also need to update events DB with dishes
    return redirect(url_for('routes.show_event', id=id))

@routes.route('/events/<int:id>')
def show_event(id):
    db = get_db()
    event = get_event_by_id(id)
    guests = get_guests_by_event_id(id)
    dishesIndex = event.keys().index('dishesToBring')
    dishesToBring = event[dishesIndex].split(',')

    if (event is None):
        return "event not found!" #TODO make a dope-ass 404 page 
    
    return render_template('event.html', 
        event=event,
        dishesToBring=dishesToBring, 
        guests=guests,
        guestCreationEndpoint="/events/" + str(id) + "/guest", #idk maybe this can be done in html directly
        numGuests=len(guests)
    )

@routes.route('/events', methods=['POST', 'GET'])
def handle_event():
    if request.method == 'POST':
        create_event(request.form)
        return redirect(url_for('routes.show_event', id=1)) #TODO get autoincremented event number
    elif request.method == 'GET':
        return render_template('events.html', events=list_events())

def list_events():
    db = get_db()
    q = db.execute("""select * from events order by id desc""")
    return q.fetchall()


def create_event(form):
    db = get_db()
    eventDatetime = 0 #TODO convert event date & time into epoch datetime
    acceptCash = 1 if form['acceptCash'] else 0
    db.execute("""insert into events (
        name, 
        location,
        description,
        datetime,
        hostName,
        hostEmail,
        dishesToBring,
        acceptCash,
        cashAmount,
        created_at,
        updated_at
    ) values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""", [
        form['name'], 
        form['location'],
        form['description'],
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
    return;

def get_event_by_id(id):
    db = get_db()
    q = db.execute("""select * from events where id = ?""", [id])
    return q.fetchone()

def get_guests_by_event_id(id):
    db = get_db()
    q = db.execute("""select * from guests where event_id = ?""", [id])
    return q.fetchall()
