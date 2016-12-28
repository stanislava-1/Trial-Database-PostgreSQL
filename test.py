import testDB

# Other modules used to run a web server.
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
  </head>
  <body>
    <h1>Test DB</h1>
    <h2>Insert New Student</h2>
    <form method=post action="/inserted">
      <label>
          First Name <input type="text" name="first_name">
      <label>
      <label>
          Last Name <input type="text" name="last_name">
      <label>
      <label>
          Gender 
          <select type="text" name="gender">
              <option>male</option>
              <option>female</option>
          </select>
      <label>
      <label>
          Country
          <input type="text" name="country">
      <label>    
      <input type="submit" value="Insert Student">
    </form>
    <p style="color:red">%(err_A)s</p>
    <h2>Delete Student</h2>
    <form method=post action="/deleted">
       <label>
          Insert student ID <input type="text" name="id">
      <label>
      <input type="submit" value="Delete Student">
    </form>
    <p style="color:red">%(err_B)s</p>
    <h2>List of students</h2>
    <div>%(all)s</div>
    <h2>Number of All Students</h2>
    <div>%(num)s</div>
    <h2>Number of Students by Gender</h2>
    <div>%(gender)s</div>
    <h2>Number of Students by Country</h2>
    <div>%(country)s</div>
  </body>
</html>
'''

# HTML templates for the results and errors
ALL = '''\
    <div><span>%(id)s</span>. <span>%(first_name)s</span> <span>%(last_name)s</span>, <span>%(gender)s</span>, <span>%(country)s</span></div>
'''
COUNT_ALL = '''\
    <div><span>All students</span>: <span>%s</span></div>
'''

GENDER_COUNT = '''\
    <div><span>%(gender)s</span>: <span>%(count)s</span></div>
'''
COUNTRY_COUNT = '''\
    <div><span>%(country)s</span>: <span>%(count)s</span></div>
'''

ERROR_A = ''

ERROR_B = ''


## Request handler for main page
def View(env, resp):
    allStudents = testDB.GetAllStudents()
    countAll = testDB.CountAll()
    genderCount = testDB.GenderCount()
    countryCount = testDB.CountryCount()

    headers = [('Content-type', 'text/html')]
    resp('200 OK', headers)

    return [HTML_WRAP % {'err_A': ERROR_A, 
                         'err_B': ERROR_B, 
                         'all': ''.join(ALL % p for p in allStudents), 
                         'num': COUNT_ALL % countAll,
                         'gender': ''.join(GENDER_COUNT % p for p in genderCount),
                         'country': ''.join(COUNTRY_COUNT % p for p in countryCount)}]

## Insert data
def Insert(env, resp):
    global ERROR_A
    input = env['wsgi.input']
    length = int(env.get('CONTENT_LENGTH', 0))
    # If length is zero, post is empty - don't save it.
    if length > 0:
        postdata = input.read(length)
        fields = cgi.parse_qs(postdata)
        if len(fields) == 4:
          first_name = fields['first_name'][0]
          last_name = fields['last_name'][0]
          gender = fields['gender'][0]
          country = fields['country'][0]
        
          # Save it in the database
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

## Delete data
def Delete(env, resp):
    global ERROR_B    
    input = env['wsgi.input']
    length = int(env.get('CONTENT_LENGTH', 0))
   
    if length > 0:
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

## Dispatch table - maps URL prefixes to request handlers
DISPATCH = {'': View,
            'inserted': Insert,
            'deleted': Delete
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


# Run this bad server only on localhost!
httpd = make_server('', 8000, Dispatcher)
print "Serving HTTP on port 8000..."
httpd.serve_forever()

