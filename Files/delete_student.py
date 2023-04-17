import sqlite3

def delete_student(id):
    try:
        c = sqlite3.connect("college.db")
        cursor = c.cursor()
        sql = "delete from students where id=?"
        cursor.execute(sql,(id,))
        c.commit()
        if cursor.rowcount > 0:
            return "Student was successfully deleted from database"
        else: 
            return "Student not found"
        
    except Exception as e:
        return "Couldn't delete student "+str(e)
    finally:
        cursor.close()
        c.close()

id1 = input("Student's id: ")
print(delete_student(id1))