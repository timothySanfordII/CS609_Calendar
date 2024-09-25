from flask import Flask, render_template, request, jsonify
import sqlite3
from datetime import datetime, timedelta

app = Flask(__name__)

# Database setup
def init_db():
    conn = sqlite3.connect('calendar.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS events (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT NOT NULL,
            event TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/events/<date>', methods=['GET', 'POST'])
def events(date):
    conn = sqlite3.connect('calendar.db')
    cursor = conn.cursor()

    if request.method == 'POST':
        event_data = request.json
        event = event_data.get('event')

        if not event:
            return jsonify(success=False, message='Event name is required.')

        cursor.execute('INSERT INTO events (date, event) VALUES (?, ?)', (date, event))
        conn.commit()
        conn.close()
        return jsonify(success=True)

    cursor.execute('SELECT id, event FROM events WHERE date = ?', (date,))
    day_events = cursor.fetchall()
    conn.close()

    return {'events': [{'id': event[0], 'name': event[1]} for event in day_events]}  # Return events as JSON

@app.route('/delete-event/<int:event_id>', methods=['DELETE'])
def delete_event(event_id):
    conn = sqlite3.connect('calendar.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM events WHERE id = ?', (event_id,))
    conn.commit()
    conn.close()
    return jsonify(success=True)

@app.route('/month-events')
def get_month_events():
    conn = sqlite3.connect('calendar.db')
    cursor = conn.cursor()
    
    today = datetime.now()
    start_date = today.replace(day=1)
    end_date = (start_date + timedelta(days=32)).replace(day=1) - timedelta(days=1)
    
    cursor.execute('SELECT date FROM events WHERE date BETWEEN ? AND ?', (start_date.strftime('%Y-%m-%d'), end_date.strftime('%Y-%m-%d')))
    month_events = cursor.fetchall()
    
    conn.close()
    return {date[0]: True for date in month_events}

if __name__ == '__main__':
    init_db()  # Initialize the database
    app.run(debug=True)
