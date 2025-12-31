#Select data from table

import mysql.connector

dass = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "root",
    database = "expense_tracker3"
)

cursor = dass.cursor()   #creating cursor object

# cursor.execute("SELECT * FROM expenses")   #select all data from the database table
cursor.execute("SELECT date, amount FROM expenses ")   #select specific data from the database table

# cursor = cursor.fetchall()   #fetch all the rows from the executed query
# cursor = cursor.fetchone()   #fetch only one row from the executed query
cursor = cursor.fetchmany()    #fetch first 5 rows from the executed query

for row in cursor:   #iterating through the rows
    print(row)    #printing each row