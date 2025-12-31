# select data from table to ORDER BY

import mysql.connector

dass = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "root",
    database = "expense_tracker3"
)

mycursor = dass.cursor()

# sql = "SELECT * FROM expenses ORDER BY amount ASC"   #sql query to select data ordered by amount in ascending order
sql = "SELECT * FROM expenses ORDER BY date DESC"   #sql query to select data ordered by date in descending order

mycursor.execute(sql)

mycursor = mycursor.fetchall()

for row in mycursor:
    print(row)
