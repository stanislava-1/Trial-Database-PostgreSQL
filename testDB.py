import psycopg2

## Database connection
DB = []

# Show all sutudents data from the table students
def GetAllStudents():
    DB = psycopg2.connect("dbname=test")
    c = DB.cursor()
    c.execute("select * from students")
    allStudents = ({'id': str(row[0]), 'first_name': str(row[1]), 'last_name': str(row[2]), 'gender': str(row[3]), 'country': str(row[4])} for row in c.fetchall())
    DB.close()
    return allStudents

# Insert new student to the table students
def InsertNewStudent(first_name, last_name, gender, country):
    DB = psycopg2.connect("dbname=test")
    c = DB.cursor()
    c.execute("insert into students (first_name, last_name, gender, country) values (%s, %s, %s, %s)", (first_name, last_name, gender, country))
    DB.commit()
    DB.close()

# Detect if the entered ID si in the table students
def IsInTable(ID):
    DB = psycopg2.connect("dbname=test")
    c = DB.cursor()
    c.execute("select * from students where id=%s", (ID,))
    result = c.fetchall()
    if result:
        return True
    else:
        return False

# Delete a student from the table students, according to entered ID
def DeleteStudent(ID):
    DB = psycopg2.connect("dbname=test")
    c = DB.cursor()
    c.execute("delete from students where id=%s", (ID,))
    DB.commit()
    DB.close()

# Count all students in the table students
def CountAll():
    DB = psycopg2.connect("dbname=test")
    c = DB.cursor()
    c.execute("select count(*) from students")
    count = c.fetchone()
    DB.close()
    return count

# Count how many of the students are males and how many of them are females
def GenderCount():
    DB = psycopg2.connect("dbname=test")
    c = DB.cursor()
    c.execute("select gender, count(*) from students group by gender")
    genderCount = ({'gender': str(row[0]), 'count': str(row[1])} for row in c.fetchall())
    DB.close()
    return genderCount

# Count how many students come from different countries
def CountryCount():
    DB = psycopg2.connect("dbname=test")
    c = DB.cursor()
    c.execute("select country, count(*) as c from students group by country order by c desc")
    countryCount = ({'country': str(row[0]), 'count': str(row[1])} for row in c.fetchall())
    DB.close()
    return countryCount

# Show only data of students of the selected gender (male or female) from the table students
# def StudentsByGender(gender):
#     DB = psycopg2.connect("dbname=test")
#     c = DB.cursor()
#     c.execute("select * from students where gender=%s", (gender,))
#     result = ({'id': str(row[0]), 'first_name': str(row[1]), 'last_name': str(row[2]), 'gender': str(row[3])} for row in c.fetchall())
#     DB.close()
#     return result

