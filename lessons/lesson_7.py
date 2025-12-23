import sqlite3


def create_tables(connection):
    connection.execute("""
    DROP TABLE IF EXISTS students
    """)
    connection.execute("""
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER DEFAULT 0,
        city TEXT
    )
    """)
def add_student(connection, name, age, city):
    connection.execute("""
    INSERT INTO students (name, age, city)
    VALUES (?,?,?)
    """,
                       (name, age, city))
    connection.commit()

def delete_student(connection, student_id):
    connection.execute("""
    DELETE FROM students WHERE id = ?
    """,
    (student_id,))
    connection.commit()
def get_all_students(connection):
    result = connection.execute(
        "SELECT ID, name FROM students "
    )
    return result.fetchall()
def get_student(connection, student_id):
    result = conn.execute(
        """SELECT * FROM students WHERE id = ?""",
        (student_id,)

    )
    return result.fetchall()
def get_students_by_city(connection, city):
    result = conn.execute(
        """
        SELECT * FROM students 
        WHERE city = ?
        ORDER BY age 
        """,
        (city,)
    )
    return result.fetchall()

def change_student(connection, student_id, name, age, city):
    connection.execute("""
    UPDATE students SET name = ?, age = ?, city = ? WHERE id = ?
    """,
                       (name, age, city, student_id))
    connection.commit()
if __name__ == '__main__':
    conn = sqlite3.connect("database.db")

    create_tables(conn)
    add_student(conn, name="Elvira", age=18, city="Talas")
    add_student(conn, name="Jimin", age=20, city="Seul")
    add_student(conn, name="Aki", age=20, city="Bishkek")
    add_student(conn, name="Saadat", age=20, city="Talas")

    delete_student(conn,1)
    print(get_all_students(conn))
    for student in get_all_students(conn):
        print(student)
    # for st in get_all_students(conn):
    #     print(st)

    print(get_student(conn, 20))
    print(get_students_by_city(conn, "Talas"))

    change_student(conn, 3, "Kimi", 29, "Rom")
    print(get_student(conn, 3))
    conn.close()
