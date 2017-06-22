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

## Step 3: Database Dump
Download the [database dump SQL file](https://github.com/bchiang7/CS3200-Project/blob/master/data/projectdump.sql) and import the data from the self-contained file in MySQL Workbench via the Server menu dropdown.
```
Server > Data Import
```

Note: Database dump file contains stored procedures as well as the create schema and data.

## Step 4: Running the project
Once you have cloned this repository and navigated to the directory in your terminal, simply run
```
python run.py
```
to start the project. Enter your MySQL username and password, and then navigate to `localhost:5000` in your browser.


## UML Diagram
![](https://raw.githubusercontent.com/bchiang7/CS3200-Project/master/img/finalUML.jpg)


## Flow Chart
![](https://raw.githubusercontent.com/bchiang7/CS3200-Project/master/img/flowchart.png)
