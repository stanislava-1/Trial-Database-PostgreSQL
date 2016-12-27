import psycopg2

## Database connection
DB = []

def GetAllStudents():
    DB = psycopg2.connect("dbname=test")
    c = DB.cursor()
    c.execute("select * from students")
    allStudents = ({'id': str(row[0]), 'first_name': str(row[1]), 'last_name': str(row[2]), 'gender': str(row[3])} for row in c.fetchall())
    DB.close()
    return allStudents

def InsertNewStudent(first_name, last_name, gender):
    DB = psycopg2.connect("dbname=test")
    c = DB.cursor()
    c.execute("insert into students (first_name, last_name, gender) values (%s, %s, %s)", (first_name, last_name, gender,))
    DB.commit()
    DB.close()

def GenderCount():
    DB = psycopg2.connect("dbname=test")
    c = DB.cursor()
    c.execute("select gender, count(*) from students group by gender")
    genderCount = ({'gender': str(row[0]), 'count': str(row[1])} for row in c.fetchall())
    DB.close()
    return genderCount

def StudentsByGender(gender):
    DB = psycopg2.connect("dbname=test")
    c = DB.cursor()
    c.execute("select * from students where gender=%s", (gender,))
    result = ({'id': str(row[0]), 'first_name': str(row[1]), 'last_name': str(row[2]), 'gender': str(row[3])} for row in c.fetchall())
    DB.close()
    return result

