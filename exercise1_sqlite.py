import sqlite3

connection = sqlite3.connect("users_sqlite.db")

cursor = connection.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS Users (
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT,
    last_name TEXT,
    email_address TEXT
)''')

usersInsertion = [
    ("Matthew", "Thomas", "mthomas@team.com"),
    ("Andrew", "Stift", "astift@team.com"),
    ("Dave", "Brown", "davebr@team.com"),
    ("Sandra", "Paddy", "sanddy@team.com"),
    ("Christabel", "Anderson", "canderson@team.com")
]

cursor.executemany(
    '''INSERT INTO Users(first_name, last_name, email_address) VALUES (?, ?, ?)''', usersInsertion)

cursor.execute("SELECT email_address FROM Users")
print(cursor.fetchall())

cursor.execute("SELECT * FROM Users")
print(cursor.fetchall())

connection.commit()
connection.close()
