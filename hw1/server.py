from bottle import get, post, route, run, template, view, static_file

@get('/index')
def index():
    return "Welcome to CMPS 183!"

@get('/greet/<input_name>')
def greet(input_name):
    return template('greet_template', name=input_name)

@view('greet_template')
@get('/sayhi/<name>')
def greet(name):
    return dict(name=name)


@get('/example')
def example():
    return template('html_example')

@get('/')
def news():
    return template('news_template')


# Our cat web page
@get('/cats')
def cats():
    return template('cats_template')

# Let's add some code to serve jpg images from our static images directory.
@post('/images/<filename:re:.*\.jpg>')
def serve_image(filename):
    return static_file(filename, root='images', mimetype='image/jpg')

# Let's add some code to serve jpg images from our static images directory.
@get('/images/<filename:re:.*\.jpg>')
def serve_image(filename):
    return static_file(filename, root='images', mimetype='image/jpg')

@route('/images/<filename:re:.*\.png>')
def serve_image(filename):
    return static_file(filename, root='images', mimetype='image/png')

# Code for serving css stylesheets from /css directory.
@route('/css/<filename:re:.*.css>')
def serve_css(filename):
    return static_file(filename, root='css', mimetype='text/css')

run(host='localhost', port=8080, debug=True)

