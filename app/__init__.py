import flask
from flask import Flask, render_template, request, jsonify, url_for
from collections import defaultdict
import pymysql
from array import array
#%% Simple selector (MySQL database)
# import mysql.connector needs to be installed pip install mysql-connector
import mysql.connector

# Prompt user for mysql username and password
username = raw_input('MySQL Username: ')
password = raw_input('MySQL Password: ')

# Connect to DB
db = pymysql.connect(host='localhost', user=username, password=password, db='top500Info', charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)

print 'Connected to database!'

# init cursors
cursor1 = db.cursor()
cursor2 = db.cursor()
cursor3 = db.cursor()
cursor4 = db.cursor()
cursor5 = db.cursor()
cursor6 = db.cursor()
filterCursor = db.cursor()

# declare app
app = Flask(__name__, instance_relative_config=True)

# Get all continent names
def getContinents():
    continents_stmt = 'SELECT DISTINCT continent_name FROM continent'
    cursor1.execute(continents_stmt)
    continents = cursor1.fetchall()
    continent_names = []
    for row in continents:
        continent_names.append(row['continent_name'])

    return continent_names

# Get all distinct climates
def getClimates():
    climates_stmt = 'SELECT DISTINCT climate FROM continent ORDER BY climate'
    cursor2.execute(climates_stmt)
    climates = cursor2.fetchall()
    climate_names = []
    for row in climates:
        climate_names.append(row['climate'])

    return climate_names

# Get all country names
def getCountries():
    countries_stmt = 'SELECT DISTINCT cname FROM country ORDER BY cname'
    cursor3.execute(countries_stmt)
    countries = cursor3.fetchall()
    country_names = []
    for row in countries:
        country_names.append(row['cname'])

    return country_names

# Get all distinct categories
def getCategories():
    categories_stmt = 'SELECT DISTINCT category FROM attraction ORDER BY category'
    cursor4.execute(categories_stmt)
    categories = cursor4.fetchall()
    category_names = []
    for row in categories:
        category_names.append(row['category'])

    return category_names

# Get all distinct origins
def getOrigins():
    origins_stmt = 'SELECT DISTINCT origin FROM attraction'
    cursor5.execute(origins_stmt)
    origins = cursor5.fetchall()
    origin_names = []
    for row in origins:
        origin_names.append(row['origin'])

    return origin_names

# Get all attraction names
def getAttractionNames():
    names_stmt = 'SELECT name FROM attraction ORDER BY name'
    cursor6.execute(names_stmt)
    names = cursor6.fetchall()
    att_names = []
    for row in names:
        att_names.append(row['name'])

    return att_names


# index page (homepage)
@app.route('/')
def db():
    continents = getContinents()
    climates = getClimates()
    countries = getCountries()
    categories = getCategories()
    origins = getOrigins()

    return render_template('index.html', continents=continents, climates=climates, countries=countries, categories=categories, origins=origins)

# Filter results page
@app.route('/filter', methods=['GET', 'POST'])
def filter():
    continent = str(request.form.get('continent'))
    climate = str(request.form.get('climate'))
    country = str(request.form.get('country'))
    category = str(request.form.get('category'))
    origin = str(request.form.get('origin'))

    filterItems = [continent, climate, country, category, origin]

    params = []
    for item in filterItems:
        if 'All' in item:
            item = ''
            params.append(item)
        else:
            params.append(item)

    results = filterAttractions( params )
    return render_template('filter.html', filterItems=filterItems, results=results)


def filterAttractions( params ):
    continent = params[0]
    climate = params[1]
    country = params[2]
    category = params[3]
    origin = params[4]
    headers = [' continent = ', ' climate = ', ' countryN = ', ' category = ', ' origin = ']

    conditions = ''
    i = 0
    for col in params:
        if col != '':
            conditions += headers[i]
            conditions += '"' + col + '"'
            conditions += ' AND'
        i += 1

    stmt = "SELECT * FROM attraction WHERE "
    cond = conditions[:-4]
    orderby = " ORDER BY attract_id"

    # concat strings to create full select statement based on user inputs
    select_stmt = stmt + cond + orderby
    filterCursor.execute(select_stmt)
    results = filterCursor.fetchall()
    result_arr = []
    for row in results:
        values = row.values()
        result_arr.append(values)

    return result_arr


# Create a visitor page
@app.route('/visitor')
def visitor():
    countries = getCountries()
    return render_template('visitor.html', countries=countries)


# New visitor page
@app.route('/profile', methods=['GET', 'POST'])
def createVisitor():
    firstname = str(request.form.get('firstname'))
    lastinitial = str(request.form.get('lastinitial'))
    age = str(request.form.get('age'))
    homecountry = str(request.form.get('homecountry'))

    newVisitor = [firstname, lastinitial, age, homecountry]

    print newVisitor

    # call SQL procedure

    # generate unique visitor ID

    # select tuple with this ID and display information


    return render_template('profile.html')

# Update visitor page
@app.route('/updateVisitor', methods=['GET', 'POST'])
def updateVisitor():
    firstname = str(request.form.get('firstname'))
    lastinitial = str(request.form.get('lastinitial'))
    age = str(request.form.get('age'))
    homecountry = str(request.form.get('homecountry'))

    newVisitor = [firstname, lastinitial, age, homecountry]

    print newVisitor

    # call SQL procedure

    # generate unique visitor ID

    # select tuple with this ID and display information


    return render_template('profile.html')


# Write a review page
@app.route('/review')
def review():
    attractions = getAttractionNames()
    return render_template('review.html', attractions=attractions)


# New review page
@app.route('/reviews', methods=['GET', 'POST'])
def createReview():
    visitorID = str(request.form.get('visitorID'))
    visited = str(request.form.get('visited'))
    dateVisited = str(request.form.get('dateVisited'))
    overall = str(request.form.get('overall'))
    family = str(request.form.get('family'))
    adventure = str(request.form.get('adventure'))

    newReview = [visitorID, visited, dateVisited, overall, family, adventure]

    print newReview

    # call SQL procedure

    # generate unique visitor ID

    # select tuple with this visitor ID and display information


    return render_template('reviews.html')



# In-class presentation page
@app.route('/presentation')
def presentation():
    return render_template('presentation.html')



# Load the config file
app.config.from_object('config')
