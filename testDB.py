import psycopg2

## Database connection
DB = []

# Show all sutudents data from the table students
def GetAllStudents():
    DB = psycopg2.connect("dbname=test")
    c = DB.cursor()
    c.execute("select students.*, enrolments.course_id \
               from students \
               left join enrolments \
               on students.id=enrolments.student_id \
               order by students.id")
    result = c.fetchall()
    allStudents = ({'ID': str(row[0]), 
                    'first_name': str(row[1]), 
                    'last_name': str(row[2]), 
                    'gender': str(row[3]), 
                    'country': str(row[4]),
                    'courses': [str(row[5])]} for row in result)
    r = 0
    for row in result:
        r += 1
    DB.close()
    allStudents_grouped = []
    allStudents_grouped.append(allStudents.next()) 
    for i in range(1, r):
        last_row = allStudents_grouped[-1]
        crs_list = last_row['courses']
        evaluated = allStudents.next()        
        if evaluated['ID'] == last_row['ID']:
            crs_list += evaluated['courses']
        else:
            crs_list.sort()
            last_row['courses'] = (', ').join(crs_list)            
            allStudents_grouped.append(evaluated)
    allStudents_grouped[-1]['courses'] = (', ').join(allStudents_grouped[-1]['courses'])
    return allStudents_grouped

# Insert new student to the table students
def InsertNewStudent(first_name, last_name, gender, country):
    DB = psycopg2.connect("dbname=test")
    c = DB.cursor()
    c.execute("insert into students (first_name, last_name, gender, country) \
               values (%s, %s, %s, %s)", (first_name, last_name, gender, country,))
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

# Enrol a student with entered ID for a selected course
def CourseEnrolment(student_id, course_id):
    DB = psycopg2.connect("dbname=test")
    c = DB.cursor()
    c.execute("insert into enrolments values (%s, %s)", (student_id, course_id,))
    DB.commit()
    DB.close()

# Update student's data
def UpdateStudentsData(ID, column, new_value):
    DB = psycopg2.connect("dbname=test")
    c = DB.cursor()
    c.execute("update students set %s" % column + "=%s \
               where id=%s", (new_value, ID,))
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
def CountGender():
    DB = psycopg2.connect("dbname=test")
    c = DB.cursor()
    c.execute("select gender, count(*) from students group by gender")
    countGender = ({'gender': str(row[0]), 'count': str(row[1])} for row in c.fetchall())
    DB.close()
    return countGender

# Count how many students come from different countries
def CountCountry():
    DB = psycopg2.connect("dbname=test")
    c = DB.cursor()
    c.execute("select country, count(*) as c from students group by country order by c desc")
    countCountry = ({'country': str(row[0]), 'count': str(row[1])} for row in c.fetchall())
    DB.close()
    return countCountry

# Count how many students are enrolled for particular courses
def CountEnrolments():
    DB = psycopg2.connect("dbname=test")
    c = DB.cursor()
    c.execute("select courses.name, count(enrolments.course_id) as c\
               from courses join enrolments \
               on courses.id=enrolments.course_id \
               group by courses.name \
               order by c desc")
    countEnrolments = ({'crs_name': str(row[0]), 'enrl_count': str(row[1])} for row in c.fetchall())
    DB.close()
    return countEnrolments


