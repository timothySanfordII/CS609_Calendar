import sqlite3

def setup_database():
    conn = sqlite3.connect("events.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS events (
            id INTEGER PRIMARY KEY,
            event_date TEXT NOT NULL,
            event_description TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

def save_event_to_db(event_date, event_description):
    conn = sqlite3.connect("events.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO events (event_date, event_description) VALUES (?, ?)", (event_date, event_description))
    conn.commit()
    conn.close()

def get_events_for_month(year, month):
    conn = sqlite3.connect("events.db")
    cursor = conn.cursor()
    cursor.execute("""
        SELECT id, event_date, event_description 
        FROM events 
        WHERE strftime('%Y', event_date) = ? AND strftime('%m', event_date) = ?
    """, (str(year), f"{month:02d}"))
    events = cursor.fetchall()
    conn.close()
    return events

def update_event_in_db(event_id, new_date, new_description):
    conn = sqlite3.connect("events.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE events SET event_date = ?, event_description = ? WHERE id = ?", (new_date, new_description, event_id))
    conn.commit()
    conn.close()

def delete_event_from_db(event_id):
    conn = sqlite3.connect("events.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM events WHERE id = ?", (event_id,))
    conn.commit()
    conn.close()