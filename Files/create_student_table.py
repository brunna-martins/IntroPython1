import sqlite3

# create table
def create_student_table():
    try:
        c = sqlite3.connect("college.db")
        cursor = c.cursor()
        sql = "create table students(id text primary key,name text,course text)"
        cursor.execute(sql)
        c.commit()
        return "Student table successfully created"
    except Exception as e:
        return "Table students already exists "+str(e)
    finally:
        cursor.close()
        c.close()

print(create_student_table())