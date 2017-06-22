# DBMS for Lonely Planet's Top 500 Ultimate Travel Destinations
By Brittany Chiang (bchiang7) & Isabel Tripp (tahitihat)

## Step 1: Prerequisites
[Python 2.7.13](https://www.python.org/downloads/)

(unfortunately mysql-connector is not backwards compatible with 3.6)

If you already have python 3.6.* installed on your computer, it's probably easiest to download [virtualenv](https://virtualenv.pypa.io/en/stable/) or [pyenv](https://github.com/pyenv/pyenv) to manage python versions.

## Step 2: Required Python Modules
[flask](http://flask.pocoo.org/): `pip install flask`

[pymysql](https://github.com/PyMySQL/PyMySQL): `pip install pymysql`

mysql-connector: `pip install mysql-connector`

## Step 3: Import the schema
Download the [project SQL file](https://github.com/bchiang7/CS3200-Project/blob/master/db_relations.sql) and open it in MySQL Workbench. Execute the file and ensure `top500Info` database has been created.

## Step 4: Import Database Dump
Download the [database dump SQL file](https://github.com/bchiang7/CS3200-Project/blob/master/data/projectdump.sql) and import the data from the self-contained file in MySQL Workbench via the Server menu dropdown.
```
Server > Data Import
```
Make sure that the Default Target Schema is `top500Info`

Once the import has completed, the tables in `top500Info` should contain tuples.

Note: Database dump file contains stored procedures as well as the create schema and data.

## Step 5: Running the project
Once you have cloned this repository and navigated to the directory in your terminal, simply run
```
python run.py
```
Enter your MySQL username and password, and then navigate to `localhost:5000` in your browser.


## UML Diagram
![](https://raw.githubusercontent.com/bchiang7/CS3200-Project/master/img/finalUML.jpg)


## Flow Chart
![](https://raw.githubusercontent.com/bchiang7/CS3200-Project/master/img/flowchart.png)
