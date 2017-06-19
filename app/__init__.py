import flask
from flask import Flask, render_template, request, jsonify, url_for
from collections import defaultdict
import pymysql
from array import array
#%% Simple selector (MySQL database)
# import mysql.connector needs to be installed pip install mysql-connector
import mysql.connector
# import MySQLdb

print '*******************************************************************'
print 'Hello! Welcome to our project. Please provide your MySQL username and password.'
username = raw_input('MySQL Username: ')
password = raw_input('MySQL Password: ')

# db = MySQLdb.connect('localhost', username, password, 'top500Info', charset='utf8', use_unicode=True)

db = pymysql.connect(host='localhost', user=username, password=password,
             db='top500Info',charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)

print 'Connected to database! Please navigate to localhost:5000 in your browser.'

cursor1 = db.cursor()
cursor2 = db.cursor()
cursor3 = db.cursor()
cursor4 = db.cursor()
cursor5 = db.cursor()
filterCursor = db.cursor()

app = Flask(__name__, instance_relative_config=True)



def getContinents():
    continents_stmt = 'SELECT DISTINCT continent_name FROM continent'
    cursor1.execute(continents_stmt)
    continents = cursor1.fetchall()
    continent_names = []
    for row in continents:
        continent_names.append(row['continent_name'])

    return continent_names


def getClimates():
    climates_stmt = 'SELECT DISTINCT climate FROM continent ORDER BY climate'
    cursor2.execute(climates_stmt)
    climates = cursor2.fetchall()
    climate_names = []
    for row in climates:
        climate_names.append(row['climate'])

    return climate_names


def getCountries():
    countries_stmt = 'SELECT DISTINCT cname FROM country ORDER BY cname'
    cursor3.execute(countries_stmt)
    countries = cursor3.fetchall()
    country_names = []
    for row in countries:
        country_names.append(row['cname'])

    return country_names

def getCategories():
    categories_stmt = 'SELECT DISTINCT category FROM attraction ORDER BY category'
    cursor4.execute(categories_stmt)
    categories = cursor4.fetchall()
    category_names = []
    for row in categories:
        category_names.append(row['category'])

    return category_names

def getOrigins():
    origins_stmt = 'SELECT DISTINCT origin FROM attraction'
    cursor5.execute(origins_stmt)
    origins = cursor5.fetchall()
    origin_names = []
    for row in origins:
        origin_names.append(row['origin'])

    return origin_names


@app.route('/')
def db():
    continents = getContinents()
    climates = getClimates()
    countries = getCountries()
    categories = getCategories()
    origins = getOrigins()

    return render_template('index.html', continents = continents, climates = climates, countries = countries, categories = categories, origins = origins)


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

    select_stmt = stmt + cond + orderby
    filterCursor.execute(select_stmt)
    results = filterCursor.fetchall()
    result_arr = []

    for row in results:
        values = row.values()
        result_arr.append(values)

    return result_arr


@app.route('/visitor')
def visitor():
    return render_template('visitor.html')


@app.route('/review')
def review():
    return render_template('review.html')


@app.route('/presentation')
def presentation():
    return render_template('presentation.html')



# Load the config file
app.config.from_object('config')
