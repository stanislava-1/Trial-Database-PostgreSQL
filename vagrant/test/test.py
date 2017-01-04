# coding=utf-8

import testDB

# Modules used to run a web server.
import cgi
from wsgiref.simple_server import make_server
from wsgiref import util

# HTML template for the page
HTML_WRAP = open('index.html').read()

# HTML templates for results and errors
SELECTED = "ID"
ALL = '''\
    <tr>
        <td class="ID">%(ID)s</td>
        <td>%(first_name)s</td>
        <td>%(last_name)s</td>
        <td>%(age)s</td>
        <td>%(gender)s</td>
        <td>%(country)s</td>
        <td>%(courses)s</td>
    </tr>
'''
COUNT_ALL = '''\
    %s students
'''
AVERAGE_AGE = '''\
    %s years
'''
MIN_AGE = '''\
    %s years
'''
MAX_AGE = '''\
    %s years
'''
AGE_COUNT = '''\
    <tr><td>%(age_interval)s:</td> <td class="number">%(count)s</td></tr>
'''
GENDER_COUNT = '''\
    <tr><td>%(gender)s:</td> <td class="number">%(count)s</td></tr>
'''
COUNTRY_COUNT = '''\
    <tr><td>%(country)s:</td> <td class="number">%(count)s</td></tr>
'''
ENROLMENTS_COUNT = '''\
    <tr><td>%(crs_name)s:</td> <td class="number">%(enrl_count)s</td></tr>
'''

ERROR_A = ''

ERROR_B = ''

ERROR_C = ''

ERROR_D = ''

ERROR_E = ''

orderBy = "students.id"

# Request handler for main page
def View(env, resp):
    global allStudents
    allStudents = testDB.GetAllStudents(orderBy)
    
    countAll = testDB.CountAll()
    averageAge = int(testDB.AverageAge()[0])
    minAge = int(testDB.Youngest()[0])
    maxAge = int(testDB.Oldest()[0])
    countAge = testDB.CountAge()
    countGender = testDB.CountGender()
    countCountry = testDB.CountCountry()
    countEnrolments = testDB.CountEnrolments()

    headers = [('Content-type', 'text/html')]
    resp('200 OK', headers)

    return [HTML_WRAP % {'sel': SELECTED,
                         'all': ''.join(ALL % p for p in allStudents),  
                         'num': COUNT_ALL % countAll,
                         'avg': AVERAGE_AGE % averageAge,
                         'min': MIN_AGE % minAge,
                         'max': MAX_AGE % maxAge,
                         'age': ''.join(AGE_COUNT % p for p in countAge),
                         'gender': ''.join(GENDER_COUNT % p for p in countGender),
                         'country': ''.join(COUNTRY_COUNT % p for p in countCountry),
                         'courses': ''.join(ENROLMENTS_COUNT % p for p in countEnrolments),
                         'err_A': ERROR_A, 
                         'err_B': ERROR_B,
                         'err_C': ERROR_C,
                         'err_D': ERROR_D,
                         'err_E': ERROR_E}]

# Order list of students by selected column
def Order(env, resp):
    global orderBy, SELECTED
    input = env['wsgi.input']
    length = int(env.get('CONTENT_LENGTH', 0))
    postdata = input.read(length)
    fields = cgi.parse_qs(postdata)
    column_names = {'students.id': 'ID', 'students.last_name': 'Last Name', 
                    'students.birthday': 'Age', 'students.gender': 'Gender',
                    'students.country': 'Country'}
    orderBy = fields['order-by'][0]
    SELECTED = column_names[orderBy]

    # 302 redirect back to the main page
    headers = [('Location', '/'),
               ('Content-type', 'text/plain')]
    resp('302 REDIRECT', headers) 
    return ['Redirecting']

# Insert student's data to the table students
def Insert(env, resp):
    global ERROR_A, ERROR_B, ERROR_C, ERROR_D, ERROR_E
    input = env['wsgi.input']
    length = int(env.get('CONTENT_LENGTH', 0))
    postdata = input.read(length)
    fields = cgi.parse_qs(postdata)
    
    if len(fields) == 5:
      first_name = fields['first_name'][0]
      last_name = fields['last_name'][0]
      birthday = fields['birthday'][0]
      gender = fields['gender'][0]
      country = fields['country'][0]    
      # Save new record in the database
      testDB.InsertNewStudent(first_name, last_name, birthday, gender, country)
      ERROR_A = ''
    else:
      if ERROR_A == '':          
        ERROR_A += 'You have to fill in all the fields. Please, try again.'

    ERROR_B = ERROR_C = ERROR_D = ERROR_E = '' 
    # 302 redirect back to the main page
    headers = [('Location', '/'),
               ('Content-type', 'text/plain')]
    resp('302 REDIRECT', headers) 
    return ['Redirecting']

# Delete student's data from database
def Delete(env, resp):
    global ERROR_A, ERROR_B, ERROR_C, ERROR_D, ERROR_E 
    input = env['wsgi.input']
    length = int(env.get('CONTENT_LENGTH', 0))
    postdata = input.read(length)
    fields = cgi.parse_qs(postdata)
    if len(fields) == 1:
      ID = fields['id'][0]
      # check if the id contains only digits and is in the DB
      if ID.isdigit() and testDB.IsInTable(ID):
        # delete record with the ID
        testDB.DeleteStudent(ID)
        ERROR_B = ''
      else:
        ERROR_B = 'Student with submitted ID is not in this database.'
    else:
      ERROR_B = 'No ID was entered.'

    ERROR_A = ERROR_C = ERROR_D = ERROR_E = '' 
    # 302 redirect back to the main page
    headers = [('Location', '/'),
               ('Content-type', 'text/plain')]
    resp('302 REDIRECT', headers) 
    return ['Redirecting'] 

# Insert student's enrolment to the table enrolments
def Enrol(env, resp):
    global ERROR_A, ERROR_B, ERROR_C, ERROR_D, ERROR_E  
    input = env['wsgi.input']
    length = int(env.get('CONTENT_LENGTH', 0))   
    postdata = input.read(length)
    fields = cgi.parse_qs(postdata)    

    if len(fields) == 2:      
      student_ID = fields['student'][0]
      course = fields['course'][0][0:4]
      course_name = fields['course'][0][5:]
      student_courses = []
      for row in allStudents:
        if row['ID'] == student_ID:
          student_courses = row['courses'].split(', ')
          break
      # check if the id contains only digits, is in the DB 
      if student_ID.isdigit() and testDB.IsInTable(student_ID):
        # check if the student is not enrolled for the selected course yet:
        if course_name not in student_courses: 
          # insert data        
          testDB.CourseEnrolment(student_ID, course)
          ERROR_C = ''
        else:
          ERROR_C = 'Student with entered ID is already enrolled for this course.'
      else:
        ERROR_C = 'Student with submitted ID is not in this database.'
    else:
      ERROR_C = 'No student ID was entered.'
    
    ERROR_A = ERROR_B = ERROR_D = ERROR_E = '' 
    # 302 redirect back to the main page
    headers = [('Location', '/'),
               ('Content-type', 'text/plain')]
    resp('302 REDIRECT', headers) 
    return ['Redirecting']

# Delete studet's enrolment for a course from the table enrolments
def Cancel_Enrol(env, resp):
    global ERROR_A, ERROR_B, ERROR_C, ERROR_D, ERROR_E   
    input = env['wsgi.input']
    length = int(env.get('CONTENT_LENGTH', 0))   
    postdata = input.read(length)
    fields = cgi.parse_qs(postdata)    

    if len(fields) == 2:      
      student_ID = fields['student'][0]
      course = fields['course'][0][0:4]
      course_name = fields['course'][0][5:]
      student_courses = []
      for row in allStudents:
        if row['ID'] == student_ID:
          student_courses = row['courses'].split(', ')
          break
      # check if the id contains only digits, is in the DB 
      if student_ID.isdigit() and testDB.IsInTable(student_ID):
        # check if the student is not enrolled for the selected course yet:
        if course_name in student_courses: 
          # insert data        
          testDB.CancelEnrolment(student_ID, course)
          ERROR_D = ''
        else:
          ERROR_D = 'Student with entered ID is not enrolled for this course.'
      else:
        ERROR_D = 'Student with submitted ID is not in this database.'
    else:
      ERROR_D = 'No student ID was entered.'

    ERROR_A = ERROR_B = ERROR_C = ERROR_E = '' 

    # 302 redirect back to the main page
    headers = [('Location', '/'),
               ('Content-type', 'text/plain')]
    resp('302 REDIRECT', headers) 
    return ['Redirecting']

# Update student's record in the table student
def Update(env, resp):
    global ERROR_A, ERROR_B, ERROR_C, ERROR_D, ERROR_E   
    input = env['wsgi.input']
    length = int(env.get('CONTENT_LENGTH', 0))
    postdata = input.read(length)
    fields = cgi.parse_qs(postdata)
    if len(fields) == 3:
      student_ID = fields['stud_ID'][0]
      column = fields['column'][0]
      new_value = fields['new_value'][0]
      
      # check if the id contains only digits and is in the DB
      if student_ID.isdigit() and testDB.IsInTable(student_ID):
        # update data
        testDB.UpdateStudentsData(student_ID, column, new_value)
        ERROR_E = ''
      else:
        ERROR_E = 'Student with submitted ID is not in this database.'
    else:
      ERROR_E = 'Not all fields were filled in.'
    
    ERROR_A = ERROR_B = ERROR_C = ERROR_D = '' 
    # 302 redirect back to the main page
    headers = [('Location', '/'),
               ('Content-type', 'text/plain')]
    resp('302 REDIRECT', headers) 
    return ['Redirecting'] 


# Dispatch table - maps URL prefixes to request handlers
DISPATCH = {'': View,
            'ordered': Order,
            'inserted': Insert,
            'deleted': Delete,
            'enrolled': Enrol,
            'updated': Update,
            'enrl-cancelled': Cancel_Enrol
        }

## Dispatcher forwards requests according to the DISPATCH table.
def Dispatcher(env, resp):
    '''Send requests to handlers based on the first path component.'''
    page = util.shift_path_info(env)
    if page in DISPATCH:
        return DISPATCH[page](env, resp)
    else:
        status = '404 Not Found'
        headers = [('Content-type', 'text/plain')]
        resp(status, headers)    
        return ['Not Found: ' + page]


# Run this server on localhost
httpd = make_server('', 8000, Dispatcher)
print "Serving HTTP on port 8000..."
httpd.serve_forever()

