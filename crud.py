import mysql.connector
from database import connect_database  


def add_student(name, age, grade, email):
    db = None
    cursor = None
    try:
        db = connect_database()
        cursor = db.cursor()
        query = """
        INSERT INTO students
        (name, age, grade, email)
        VALUES
        (%s, %s, %s, %s)
        """

        cursor.execute(query, (name, age, grade, email))
        db.commit()

        rows = cursor.rowcount

        

        return rows
    except mysql.connector.IntegrityError:
        print("Email already exists")
        return 0

    finally:
        if cursor:
            cursor.close()
        if db:
            db.close()
    


def view_student():
    db = None
    cursor = None
    try:
        db = connect_database()
        cursor = db.cursor(dictionary=True)
        query = """
        SELECT * FROM students
        """
        cursor.execute(query)
        students = cursor.fetchall()

        return students

    except Exception as e:
        print(f"Error Occured: {e}")
        return []
    
    finally:
        if cursor:
            cursor.close()
        if db:
            db.close()


def update_student_grade(new_grade, student_id):
    db = None
    cursor = None
    try:
        db = connect_database()
        cursor = db.cursor()

        query = """
        UPDATE students
        SET grade = %s
        WHERE id = %s
        """

        cursor.execute(query, (new_grade, student_id))
        db.commit()

        rows = cursor.rowcount

        return rows

    except Exception as e:
        print(f"Error Occured: {e}")
        return 0
    
    finally:
        if cursor:
            cursor.close()
        if db:
            db.close()


def delete_student(student_id):
    db = None
    cursor = None
    try:
        db = connect_database()
        cursor = db.cursor()

        query = """
        DELETE FROM students WHERE id = %s
        """
        cursor.execute(query, (student_id,))

        db.commit()
        rows = cursor.rowcount


        return rows

    except Exception as e:
        print(f"Error Occured: {e}")
        return 0

    finally:
        if cursor:
            cursor.close()
        if db:
            db.close()



