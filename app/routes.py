from app import app

#routes – URLs where a flask app accepts requests
@app.route('/')
@app.route('/index')
#a view function – route handler
def index():
    user = {'username': 'lheck'}
    return '''
<html>
    <head>
        <title>Home Page - Demo</title>
    </head>
    <body>
        <h1>Hello, ''' + user['username'] + '''!</h1>
    </body>
</html>'''
