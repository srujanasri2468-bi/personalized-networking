import sqlite3

# Connect to (or create) the SQLite database
conn = sqlite3.connect("networking.db")

# Create a cursor object
cursor = conn.cursor()

# Create the users table if it doesn't already exist
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    skills TEXT,
    interests TEXT
)
""")

# Save changes
conn.commit()

# Close the connection
conn.close()

print("✅ Database and users table created successfully!")
