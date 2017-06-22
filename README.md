# CS 3200 Final Project
By Brittany Chiang (bchiang7) & Isabel Tripp (tahitihat)

## Prerequisites
[Python 2.7.13](https://www.python.org/downloads/)

(unfortunately mysql-connector is not backwards compatible with 3.6)

If you already have python 3.6.* installed on your computer, it's probably easiest to download [virtualenv](https://virtualenv.pypa.io/en/stable/) or [pyenv](https://github.com/pyenv/pyenv) to manage python versions.

## Packages
[flask](http://flask.pocoo.org/): `pip install flask`

[pymysql](https://github.com/PyMySQL/PyMySQL): `pip install pymysql`

mysql-connector: `pip install mysql-connector`

## Database Dump
Database dump file can be found [here](https://github.com/bchiang7/CS3200-Project/blob/master/data/dump.sql)

Download the SQL file and import the data from the self-contained file in MySQL Workbench.

`Server > Data Import`

## Running the project
Once you have cloned this repository and navigated to the directory in your terminal, simply run
```
python run.py
```
to start the project and navigate to `localhost:5000` in your browser.


## UML Diagram
![](https://raw.githubusercontent.com/bchiang7/CS3200-Project/master/img/finalUML.png)


## Flow Chart
![](https://raw.githubusercontent.com/bchiang7/CS3200-Project/master/img/flowchart.png)
