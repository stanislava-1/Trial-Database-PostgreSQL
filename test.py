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
    <style>
      
    </style>
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
      
      <input type="submit" value="Insert Student">
    </form>
    <h2>All Students</h2>
    %(all)s
    <h2>Genders Count</h2>
    %(gen)s
  </body>
</html>
'''

# HTML template for the result
ALL = '''\
    <div><span>%(id)s</span>. <span>%(first_name)s</span> <span>%(last_name)s</span>, <span>%(gender)s</span></div>
'''
GENDER_COUNT = '''\
    <div><span>%(gender)s</span>: <span>%(count)s</span></div>
'''

## Request handler for main page
def View(env, resp):
    '''
    View is the 'main page'
    '''      
    allStudents = testDB.GetAllStudents()
    genderCount = testDB.GenderCount()

    headers = [('Content-type', 'text/html')]
    resp('200 OK', headers)
    return [HTML_WRAP % {'all': ''.join(ALL % p for p in allStudents), 'gen': ''.join(GENDER_COUNT % p for p in genderCount)}]

## Request handler for result
def Post(env, resp):
    
    input = env['wsgi.input']
    length = int(env.get('CONTENT_LENGTH', 0))
    # If length is zero, post is empty - don't save it.
    if length > 0:
        postdata = input.read(length)
        fields = cgi.parse_qs(postdata)
        first_name = fields['first_name'][0]
        last_name = fields['last_name'][0]
        gender = fields['gender'][0]
        
        # Save it in the database
        testDB.InsertNewStudent(first_name, last_name, gender)
    # 302 redirect back to the main page
    headers = [('Location', '/'),
               ('Content-type', 'text/plain')]
    resp('302 REDIRECT', headers) 
    return ['Redirecting']

## Dispatch table - maps URL prefixes to request handlers
DISPATCH = {'': View,
            'inserted': Post,
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

