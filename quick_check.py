import sqlite3
conn = sqlite3.connect("src/database/users.db")
cursor = conn.cursor()
cursor.execute("SELECT * FROM users")
print("Users in database:")
for row in cursor.fetchall():
    print(f"ID: {row[0]}, Username: {row[1]}, Created: {row[4] if len(row) > 4 else 'N/A'}")
conn.close()