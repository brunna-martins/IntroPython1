import sqlite3

def change_student(id,name,course):
    try:
        c = sqlite3.connect("college.db")
        cursor = c.cursor()
        sql = "update students set name=?,course=? where id=?"
        cursor.execute(sql,(name,course,id))
        c.commit()
        # verifies how many lines were successfully updated
        if cursor.rowcount > 0:
            return "Student data updated succesfully"
        else:
            "Student not found"
    except Exception as e:
        return "Couldn't update student data "+str(e)
    finally:
        cursor.close()
        c.close()

id1 = input("Student's id you would like to update data: ")
new_name = input("Student's new name: ")
new_course = input("Student's new course: ")
print(change_student(id1,new_name,new_course))