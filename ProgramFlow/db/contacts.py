import sqlite3

db = sqlite3.connect("contacts.sqlite")
db.execute("CREATE TABLE IF NOT EXISTS contacts (name TEXT, phone INTEGER, email TEXT)")
db.execute("INSERT INTO contacts(name, phone, email) VALUES('Tim', 6545678, 'tim@email.com')")
db.execute("INSERT INTO contacts VALUES('Brian', 1234, 'brian@myemail.com')")

cursor = db.cursor()

# cursor.fetchall()
cursor.fetchone()
cursor.fetchone()
cursor.fetchone()

print('*' * 80)
cursor.execute("SELECT * FROM contacts")

for name, phone, email in cursor:
    print(f"{name} : {phone} : {email}")
cursor.close()
db.commit()
db.close()