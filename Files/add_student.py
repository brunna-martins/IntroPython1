import sqlite3

def add_student(id,name,course):
    try:
        c = sqlite3.connect("college.db")
        cursor = c.cursor()
        sql = "insert into students(id,name,course) values(?,?,?)"
        cursor.execute(sql,(id,name,course))
        c.commit()
        return "Student " + name + " successfully added to database"
    except Exception as e:
        return "Failed to add student "+str(e)
    finally:
        cursor.close()
        c.close()

name1 = input("Student name: ")
id1 = input("Student id: ")
course1 = input("Student course: ")
print(add_student(id1,name1,course1))