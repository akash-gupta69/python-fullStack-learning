import sqlite3


conn = sqlite3.connect("abc.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS students(
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT NOT NULL,
age INTEGER,
grade TEXT)                              
               """)

#name = "Tom"
# web app form or sink
# sqllit3 dosn't allow multiple sql statements to run. that's why it's safe
"""name = "Tom); DROP TABLE students; --"
cursor.execute(f"INSERT INTO students (name) VALUES  ('{name}')")

conn.commit()"""

# parameterised query that prevent sql injectio attack
"""cursor.execute("insert into students (name, age, grade) values (?, ?, ?)",
                ("BOB", 22, "B++"))

conn.commit()"""
"""
cursor.execute("UPDATE students SET grade = ? WHERE id = ?",("A++",2))
conn.commit()

cursor.execute("SELECT * FROM students")
#rows = cursor.fetchall()
rows = cursor.fetchmany(2)

for row in rows:
    print(row)
"""
# DELETE DATA
"""
cursor.execute("DELETE FROM students WHERE id = ?",(4,))
conn.commit()"""


### ORDER by
#cursor.execute("SELECT * FROM students ORDER BY age")
#cursor.execute("SELECT * FROM students ORDER BY age DESC")
# cursor.execute("SELECT * FROM students ORDER BY age DESC LIMIT 2")

#Find data by pattern

cursor.execute("SELECT * FROM students WHERE name LIKE?",( '%om%'))
#cursor.execute("SELECT * FROM students")
#rows = cursor.fetchall()

rows = cursor.fetchall()

for row in rows:
    print(row)