import sqlite3

conn = sqlite3.connect('Cars.db')

cursor = conn.cursor()

cursor.execute('''
	CREATE TABLE Cars (
		Maker VARCHAR(20),
		Color VARCHAR(20),
		Year INT
	);
''')

conn.commit()
conn.close()

print("\033[92m" + "Cars table successfully created!" + "\033[0m")
