from flask import Flask
'''
It create an instance of the Flask class,
wich will be your WSGI (Web Server Gateway Interface) application.
'''
### WSGI Application
app=Flask(__name__)

@app.route("/")
def welcome():
  return "Welcome to this best Flask course. This should be an amazing course"

@app.route("/index")
def index():
  return "Welcome to the index page"



if __name__=="__main__":
  app.run(debug=True)