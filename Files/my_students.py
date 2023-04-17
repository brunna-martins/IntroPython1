import sqlite3

def my_students():
    try:
        c = sqlite3.connect("college.db")
        cursor = c.cursor()
        cursor.execute("select * from students")
        students = cursor.fetchall()
        for student in students:
            print(student)
        return "Students: "+str(len(students))
    except Exception as e:
        return "Failed to find students "+str(e)
    finally:
        cursor.close()
        c.close()

print(my_students())