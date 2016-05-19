#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
os.environ["NLS_LANG"] = "PORTUGUESE_BRAZIL.AL32UTF8"
import cx_Oracle

user = ""
password = ""
db = ""

connection = cx_Oracle.connect(user+"/"+password+"@"+db)
cursor = connection.cursor()

"""
cursor.execute("SELECT * from TABLE")
result = cursor.fetchone()
if result == None: 
        print "No result"
        exit
else:
        while result:   
                print result[0]
                result = cursor.fetchone()
"""

cursor.close()
connection.close()