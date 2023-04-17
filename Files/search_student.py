import sqlite3

def search_student(id):
    try:
        c = sqlite3.connect("college.db")
        cursor = c.cursor()
        cursor.execute("select * from students where id = ?",(id,))
        student = cursor.fetchone()
        # if I can't find a student related to this id
        if student is None:
            return "Student not found"
        else:
            return student
    except Exception as e:
        return "Failed to find students "+str(e)
    finally:
        cursor.close()
        c.close()

std_id = input("Student id: ")
print(search_student(std_id))