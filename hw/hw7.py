import sqlite3

conn = sqlite3.connect("../students.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    name TEXT,
    age INTEGER,
    course INTEGER
)
""")
conn.commit()

def create_student(name, age, course):
    cursor.execute(
        "INSERT INTO students (name, age, course) VALUES (?, ?, ?)",
        (name, age, course)
    )
    conn.commit()

def read_students():
    cursor.execute("SELECT rowid, * FROM students")
    return cursor.fetchall()

def update_student(rowid, name, age, course):
    cursor.execute(
        "UPDATE students SET name=?, age=?, course=? WHERE rowid=?",
        (name, age, course, rowid)
    )
    conn.commit()

def delete_student(rowid):
    cursor.execute("DELETE FROM students WHERE rowid=?", (rowid,))
    conn.commit()


create_student("Алексей", 18, 1)
create_student("Мария", 19, 2)

print("Все студенты:")
for student in read_students():
    print(student)

update_student(1, "Алексей", 19, 2)

delete_student(2)

print("\nПосле изменений:")
for student in read_students():
    print(student)

conn.close()