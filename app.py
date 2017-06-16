#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask
from collections import defaultdict

import pymysql
from array import array

import mysql.connector

#!/usr/bin/env python
# -*- coding: utf-8 -*-

#%% Simple selector (MySQL database)
# import mysql.connector needs to be installed pip install mysql-connector
import pymysql
import flask

cnx = pymysql.connect(host='localhost', user='root', password='root',
             db='starwarsfinaltrippi',charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor )



cur = cnx.cursor()
stmt_select = "select * from characters order by character_name"

cur.execute(stmt_select)

for row in cur.fetchall():
    print (row)
cur.close()

app = Flask(__name__)

@app.route("/")

def main():
    return "Welcome!"



if __name__ == "__main__":
    app.run()
