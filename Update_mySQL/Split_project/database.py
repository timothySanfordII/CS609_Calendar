import mysql.connector

# MySQL Database Configuration
DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',  # Replace with your MySQL username
    'password': 'tims',  # Replace with your MySQL password
    'database': '645_project'  # Replace with your database name
}

# Establish a connection to the database
def get_connection():
    return mysql.connector.connect(**DB_CONFIG)

# Database setup (create table if it doesn't exist)
def setup_database():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS events (
            id INT AUTO_INCREMENT PRIMARY KEY,
            event_date DATE NOT NULL,
            event_description TEXT NOT NULL
        )
    """)
    conn.commit()
    cursor.close()
    conn.close()

# Save an event to the database
def save_event_to_db(event_date, event_description):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO events (event_date, event_description) VALUES (%s, %s)", (event_date, event_description))
    conn.commit()
    cursor.close()
    conn.close()

# Retrieve events for the current month from the database
def get_events_for_month(year, month):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT id, event_date, event_description 
        FROM events 
        WHERE YEAR(event_date) = %s AND MONTH(event_date) = %s
    """, (year, month))
    events = cursor.fetchall()
    cursor.close()
    conn.close()
    return events

# Update an event in the database
def update_event_in_db(event_id, new_date, new_description):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE events SET event_date = %s, event_description = %s WHERE id = %s", (new_date, new_description, event_id))
    conn.commit()
    cursor.close()
    conn.close()

# Delete an event from the database
def delete_event_from_db(event_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM events WHERE id = %s", (event_id,))
    conn.commit()
    cursor.close()
    conn.close()
