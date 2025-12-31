# select data with where

import mysql.connector  #import mysql.connector module

dass = mysql.connector.connect(   #establishing the connection     
    host = "localhost",  #host name
    user = "root",  #user name
    password = "root",   #mysql password
    database = "expense_tracker3"   #database name
)

mycursor = dass.cursor()   #creating cursor object

# sql = "SELECT * FROM expenses WHERE date  = '2025-10-23'  OR  amount = 250.00"  #sql query to select data with WHERE clause using OR operater
# sql = "SELECT *  FROM expenses WHERE category = 'food' AND amount <= 1000.00"   #sql query to select data with WHERE clause using AND operater
# sql = "SELECT * FROM expenses WHERE note IS NULL"   #sql query to select data with WHERE clause using IS NULL consition
# sql = "SELECT * FROM expenses WHERE note IS NOT NULL"   #sql query to select data with WHERE clause using IS NOT NULL consition
# sql = "SELECT * FROM expenses WHERE category LIKE '%oo%'"   #sql query to select data with WHERE clause using LIKE operater
sql = "SELECT * FROM expenses WHERE amount = %s"   #sql query to select data with WHERE clause using placeholder
val = (250.00,)  #value to be substituted in the placeholder

mycursor.execute(sql, val)  #executing the sql query

mycursor = mycursor.fetchall()   #fetchiing all the rows from the executed query

for row in mycursor:   #iterating through the rows
    print(row)   #printing each row