# coding=utf-8

import testDB

# Modules used to run a web server.
import cgi
from wsgiref.simple_server import make_server
from wsgiref import util

# HTML template for the page
HTML_WRAP = '''\
<!DOCTYPE html>
<html>
  <head>
    <title>test DB</title>
    <meta charset="UTF-8">
    <style>
      body {margin: 0;}
      h1, h2, h3 {font-family: "Arial", Times New Roman;}      
      h1 {color: white; background-color: grey; margin: 0; padding: 20px;}
      h2 {margin: 0; padding: 10px; background-color: #a5d6a7}
      h3 {margin-top: 0}
      .content {padding: 20px;} 
      .part {height: 180px; display: inline-block; vertical-align: top; margin: 10px 10px 0 0; 
             padding: 15px; background-color: #ddd;}
      .col {display: inline-block; vertical-align: top; margin: 10px 40px 0 0;}
      .part-stat {margin-bottom: 15px;}
      input, select {margin-bottom: 7px;}
      table {border-collapse: collapse;}
      td {padding-right: 20px;}
      td, tr {border-bottom: 1px solid #ddd;}
      .b {font-weight: bold;}
      .ID {text-align: right;}
      .number {text-align: center;}
      .id {width: 30px;}
    </style>
  </head>
  <body>
    <h1>Test DB - Database of Students</h1>
    
      <section id="DB-all">
        <h2>List of students</h2>
        <section class="content">
          <form method="post" action="/ordered">
            <label>
              <b>Order by:</b> 
              <select name="order-by">
                <option value="students.id">ID</option>
                <option value="students.last_name">Last Name</option>
                <option value="students.birthday">Age</option>
                <option value="students.gender">Gender</option>
                <option value="students.country">Country</option>
              </select>
            </label>
            <input type="submit" value="Order">
          </form><br>
          <table>
            <tr class="b">
              <td class="ID">ID</td>
              <td>First Name</td>
              <td>Last Name</td>
              <td>Age</td>
              <td>Gender</td>
              <td>Country</td>
              <td>Courses</td>
            </tr>
            %(all)s
          </table>
        </section>
      </section>

      <section id="DB-manipulation">
        <h2>Database Manipulation</h2>
        <section class="content">   
          <section class="part">
            <h3>Insert New Student</h2>
            <form method=post action="/inserted">
              <label>
                  First Name: <input type="text" name="first_name">
              </label><br>
              <label>
                  Last Name: <input type="text" name="last_name">
              </label><br>
              <label>
                  Gender: 
                  <select type="text" name="gender">
                      <option>male</option>
                      <option>female</option>
                  </select>
              </label><br>
              <label>
                  Country:
                  <input type="text" name="country">
              </label><br>    
              <input type="submit" value="Insert Student">
            </form>
            <p style="color:red">%(err_A)s</p>
          </section>
          <section class="part">
            <h3>Delete Student</h2>
            <form method=post action="/deleted">
               <label>
                  Insert ID of a student you want to delete:
                  <input type="text" name="id" class="id">
              </label><br>
              <input type="submit" value="Delete Student">
            </form>
            <p style="color:red">%(err_B)s</p>
          </section>
          <section class="part">
            <h3>Enrol Student for a Course</h2>
            <form method=post action="/enrolled">
               <label>
                  Insert ID of a student you want to enrol for a course:
                  <input type="text" name="student" class="id">
              </label><br>
              <label>
                  Select Course:
                  <select type="text" name="course">
                      <option>C001-History</option>
                      <option>C002-Mathematics</option>
                      <option>C003-Computer Science</option>
                      <option>C004-Slovak Language</option>
                      <option>C005-Chemistry</option>
                      <option>C006-Physics</option>
                      <option>C007-English Language</option>
                      <option>C008-Journalism</option>
                      <option>C009-Painting</option>
                      <option>C010-Music Theory</option>
                      <option>C011-Creative Writing</option>
                  </select>
              </label><br>
              <input type="submit" value="Enrol">
            </form>
            <p style="color:red">%(err_C)s</p>
          </section>
          <section class="part">
            <h3>Update Student's Data</h2>
            <form method=post action="/updated">
               <label>
                  Insert ID of a student you want to update:
                  <input type="text" name="stud_ID" class="id">
              </label><br>
              <label>
                  Select what kind of data you want to update:
                  <select type="text" name="column">
                      <option value="first_name">First Name</option>
                      <option value="last_name">Last Name</option>
                      <option value="country">Country</option>
                  </select>
              </label><br>
              <label>
                  Enter new value:
                  <input type="text" name="new_value">
              </label><br>
              <input type="submit" value="Update">
            </form>
            <p style="color:red">%(err_D)s</p>
          </section>
        </section>
      </section>
      
      <section id="DB-statistics">
        <h2>Database Statistics</h2>
        <section class="content">
          <div class="col">
            <section class="part-stat">    
              <h3>Number of All Students</h3>
              <p>%(num)s</p>
            </section>
            <section class="part-stat">    
              <h3>Average Age of Students</h3>
              <p>%(avg)s</p>
            </section>
          </div>
          <div class="col">
            <section class="part-stat">
              <h3>Number of Students by Gender</h3>
              <table>
                <tr class="b"><td>Gender</td><td>Students</td></tr>
                %(gender)s
              </table>
            </section>          
            <section class="part-stat">
              <h3>Number of Students by Country</h3>
              <table>
                <tr class="b"><td>Country</td><td>Students</td></tr>
                %(country)s
              </table>
            </section>
          </div>
          <div class="col">
            <section class="part-stat">
              <h3>Number of Students Enrolled for Courses</h3>
              <table>
                <tr class="b"><td>Course</td><td>Students</td></tr>
                %(courses)s
              </table>
            </section>
          </div>
        </section>
      </section>
  </body>
</html>
'''

# HTML templates for the results and errors
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

orderBy = "students.id"

# Request handler for main page
def View(env, resp):
    global allStudents
    allStudents = testDB.GetAllStudents(orderBy)
    
    countAll = testDB.CountAll()
    averageAge = int(testDB.AverageAge()[0])
    countGender = testDB.CountGender()
    countCountry = testDB.CountCountry()
    countEnrolments = testDB.CountEnrolments()

    headers = [('Content-type', 'text/html')]
    resp('200 OK', headers)

    return [HTML_WRAP % {'all': ''.join(ALL % p for p in allStudents), 
                         'num': COUNT_ALL % countAll,
                         'avg': AVERAGE_AGE % averageAge,
                         'gender': ''.join(GENDER_COUNT % p for p in countGender),
                         'country': ''.join(COUNTRY_COUNT % p for p in countCountry),
                         'courses': ''.join(ENROLMENTS_COUNT % p for p in countEnrolments),
                         'err_A': ERROR_A, 
                         'err_B': ERROR_B,
                         'err_C': ERROR_C,
                         'err_D': ERROR_D}]

# Order list of students by selected column
def Order(env, resp):
    global orderBy
    input = env['wsgi.input']
    length = int(env.get('CONTENT_LENGTH', 0))

    postdata = input.read(length)
    fields = cgi.parse_qs(postdata)
    
    orderBy = fields['order-by'][0]

    # 302 redirect back to the main page
    headers = [('Location', '/'),
               ('Content-type', 'text/plain')]
    resp('302 REDIRECT', headers) 
    return ['Redirecting']

# Insert student's data to the table students
def Insert(env, resp):
    global ERROR_A
    input = env['wsgi.input']
    length = int(env.get('CONTENT_LENGTH', 0))
    postdata = input.read(length)
    fields = cgi.parse_qs(postdata)
    
    if len(fields) == 4:
      first_name = fields['first_name'][0]
      last_name = fields['last_name'][0]
      gender = fields['gender'][0]
      country = fields['country'][0]    
      # Save new record in the database
      testDB.InsertNewStudent(first_name, last_name, gender, country)
      ERROR_A = ''
    else:
      if ERROR_A == '':          
        ERROR_A += 'You have to fill in all the fields. Please, try again.'
    # 302 redirect back to the main page
    headers = [('Location', '/'),
               ('Content-type', 'text/plain')]
    resp('302 REDIRECT', headers) 
    return ['Redirecting']

# Delete student's data from database
def Delete(env, resp):
    global ERROR_B    
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
    # 302 redirect back to the main page
    headers = [('Location', '/'),
               ('Content-type', 'text/plain')]
    resp('302 REDIRECT', headers) 
    return ['Redirecting'] 

# Insert student's enrolment to the table enrolments
def Enrol(env, resp):
    global ERROR_C    
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

    # 302 redirect back to the main page
    headers = [('Location', '/'),
               ('Content-type', 'text/plain')]
    resp('302 REDIRECT', headers) 
    return ['Redirecting']

def Update(env, resp):
  global ERROR_D    
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
      ERROR_D = ''
    else:
      ERROR_D = 'Student with submitted ID is not in this database.'
  else:
    ERROR_D = 'Not all fields were filled in.'

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
            'updated': Update
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

