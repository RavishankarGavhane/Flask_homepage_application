from datetime import datetime
from flask import Flask

app = Flask(__name__)

counter = 0

@app.route("/")
def welcome():

    return "welcome to our application"

@app.route("/date")
def date():

    return f"This page is served at {str(datetime.now())}"

#this route his showing for number of count to our appliaction
@app.route("/count_view")
def count_view():
    global counter
    counter +=1
    return f"This page has been served - {counter} many time !!!"




