import sqlite3

# Step 1: Connect to the SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('holidays.db')

# Step 2: Create a cursor object to execute SQL commands
cursor = conn.cursor()

# Step 3: Create a table for holidays
cursor.execute('''
CREATE TABLE IF NOT EXISTS holidays (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    date TEXT NOT NULL,
    description TEXT
)
''')

# Step 4: Insert sample holiday data
holidays = [
    ('New Year\'s Day', '2024-01-01', 'Celebration of the new year.'),
    ('Independence Day', '2024-07-04', 'Celebration of the Declaration of Independence.'),
    ('Thanksgiving', '2024-11-28', 'A day for giving thanks and feasting.'),
]

cursor.executemany('INSERT INTO holidays (name, date, description) VALUES (?, ?, ?)', holidays)

# Step 5: Commit the changes
conn.commit()

# Step 6: Retrieve and display the holidays
cursor.execute('SELECT * FROM holidays')
rows = cursor.fetchall()

print("Holidays:")
for row in rows:
    print(f"ID: {row[0]}, Name: {row[1]}, Date: {row[2]}, Description: {row[3]}")

# Step 7: Close the connection
conn.close()
