from flask import Flask, render_template
from collections import defaultdict
import pymysql
from array import array
import mysql.connector
#%% Simple selector (MySQL database)
# import mysql.connector needs to be installed pip install mysql-connector
import MySQLdb

print '*******************************************************************'
print 'Hello! Welcome to our project. Please provide your MySQL username and password.'
username = raw_input('MySQL Username: ')
password = raw_input('MySQL Password: ')

db = MySQLdb.connect("localhost", username, password, "top500Info", charset="utf8", use_unicode=True)
print 'Connected to database! Please navigate to localhost:5000 in your browser.'

cursor = db.cursor()

app = Flask(__name__, instance_relative_config=True)


@app.route('/')
def db():
    all_countries = "SELECT cname FROM country"
    cursor.execute(all_countries)
    countries = cursor.fetchall()

    continents = ("Africa", "Antarctica", "Asia", "Australia", "Europe", "North America", "South America")
    climates = ("Tropical", "Cold", "Temperate")
    categories = ("Adventure/Activity", "District/Square", "Geological Feature", "Historical Site", "Modern Attractions", "Museum", "Nature Landscape", "Palace/Castle", "Religion", "Water Feature", "Wildlife")
    origins = ("Natural", "Man-made")



    return render_template('index.html', continents = continents, countries = countries, climates = climates, categories = categories, origins = origins)


@app.route('/visitor')
def visitor():
    return render_template("visitor.html")


@app.route('/review')
def review():
    return render_template("review.html")



# Load the views
# from app import views

# Load the config file
app.config.from_object('config')
