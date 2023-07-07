import sqlite3

# Establish a connection to the database
conn = sqlite3.connect('flask.db')

# Check the connection status
if conn is not None:
    print("Connection to the database successful.")
    cursor = conn.cursor()
    cursor.execute("PRAGMA database_list")
    database_info = cursor.fetchone()
    print("SQLite file location:", database_info[2])
else:
    print("Connection to the database failed.")

# Close the connection
conn.close()
