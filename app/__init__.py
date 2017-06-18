from flask import Flask, render_template
from collections import defaultdict
import pymysql
from array import array
import mysql.connector
#%% Simple selector (MySQL database)
# import mysql.connector needs to be installed pip install mysql-connector
import MySQLdb

print '\n*******************************************************************'
print 'Hello! Welcome to our project. Please provide your MySQL username and password.'
username = raw_input('MySQL Username: ')
password = raw_input('MySQL Password: ')


db = MySQLdb.connect("localhost", username, password,"top500Info")
print '\nConnected to database! Please navigate to localhost:5000 in your browser.'

cursor = db.cursor()



app = Flask(__name__, instance_relative_config=True)


@app.route('/')
def db():

    cursor.execute("SELECT * from continent")

    data = cursor.fetchall()

    return render_template('index.html', data = data)



@app.route('/review')
def review():
    return render_template("review.html")



# Load the views
# from app import views

# Load the config file
app.config.from_object('config')
