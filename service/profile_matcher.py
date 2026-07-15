import sqlite3

def get_matching_users(skill):

    conn = sqlite3.connect("networking.db")
    cursor = conn.cursor()

    cursor.execute(
        "SELECT name, email, skills FROM users WHERE skills LIKE ?",
        ('%' + skill + '%',)
    )

    users = cursor.fetchall()

    conn.close()

    return users