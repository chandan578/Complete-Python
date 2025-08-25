from flask import Flask

'''
 It creates an instance of the Flask class, 
 which will be your WSGI (Web Server Gateway Interface) application.
'''
## WSGI application
app = Flask(__name__)

# decorator
@app.route('/')
def welcome():
    return "Welcome to the flask api. This is using python to the create API in this using flask framework.."

@app.route('/index')
def index():
    return "This is our index page"

@app.route('/about')
def about():
    return "This is about page.."

if __name__ == "__main__":

    app.run(debug=True)