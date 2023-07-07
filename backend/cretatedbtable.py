import sqlite3
import datetime

# Establish a connection to the database
conn = sqlite3.connect('flask.db')

# Create a cursor object to execute SQL queries
cursor = conn.cursor()

# Create the 'Articles' table if it doesn't exist
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Articles (
        id INTEGER PRIMARY KEY,
        title TEXT,
        body TEXT,
        date DATETIME DEFAULT CURRENT_TIMESTAMP
    )
''')

# Commit the changes to the database
conn.commit()

# Check the table creation status
cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='Articles'")
table_exists = cursor.fetchone() is not None

if table_exists:
    print("Table 'Articles' created successfully.")
else:
    print("Failed to create the table 'Articles'.")

# Close the cursor and connection
cursor.close()
conn.close()
