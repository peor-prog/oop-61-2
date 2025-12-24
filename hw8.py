import sqlite3

conn = sqlite3.connect("school.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS courses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    course_name TEXT,
    student_id INTEGER,
    FOREIGN KEY (student_id) REFERENCES students(id)
)
""")

conn.commit()


def add_student(name):
    cursor.execute("INSERT INTO students (name) VALUES (?)", (name,))
    conn.commit()


def add_course(course_name, student_id):
    cursor.execute(
        "INSERT INTO courses (course_name, student_id) VALUES (?, ?)",
        (course_name, student_id)
    )
    conn.commit()


def show_students_and_courses():
    cursor.execute("""
    SELECT students.name, courses.course_name
    FROM students
    LEFT JOIN courses ON students.id = courses.student_id
    """)
    results = cursor.fetchall()

    print("\nСтуденты и их курсы:")
    for row in results:
        print(row)


def aggregate_functions():
    cursor.execute("SELECT COUNT(*) FROM courses")
    print("\nCOUNT (всего курсов):", cursor.fetchone()[0])

    cursor.execute("SELECT MAX(id) FROM students")
    print("MAX (макс. id студента):", cursor.fetchone()[0])

    cursor.execute("SELECT MIN(id) FROM students")
    print("MIN (мин. id студента):", cursor.fetchone()[0])


def courses_count_per_student():
    cursor.execute("""
    SELECT students.name, COUNT(courses.id)
    FROM students
    LEFT JOIN courses ON students.id = courses.student_id
    GROUP BY students.id
    """)
    print("\nКоличество курсов у каждого студента:")
    for row in cursor.fetchall():
        print(row)


def students_with_course(course_name):
    cursor.execute("""
    SELECT name FROM students
    WHERE id IN (
        SELECT student_id FROM courses WHERE course_name = ?
    )
    """, (course_name,))
    print(f"\nСтуденты, у которых есть курс '{course_name}':")
    for row in cursor.fetchall():
        print(row)

cursor.execute("""
    CREATE VIEW IF NOT EXISTS student_courses_view AS
    SELECT students.name, courses.course_name
    FROM students
    LEFT JOIN courses ON students.id = courses.student_id
""")
conn.commit()


def show_view():
    cursor.execute("SELECT * FROM student_courses_view")
    print("\nVIEW (student_courses_view):")
    for row in cursor.fetchall():
        print(row)

add_student("Алиса")
add_student("Боб")

add_course("Python", 1)
add_course("SQL", 1)
add_course("Math", 2)

show_students_and_courses()
aggregate_functions()
courses_count_per_student()
students_with_course("Python")
show_view()

conn.close()