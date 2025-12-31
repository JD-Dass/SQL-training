# CREATE DATABASE

import mysql.connector   # import the mysql.connector module

mydb = mysql.connector.connect(   #establish a connection to the MySql database
    host = "localhost",   #specify the host
    user = "root",   #specify the user name
    password = "root",   #specify the password
    database = "expense_tracker"   # specify the database name
)

# print("connection successful")
# mycursor = mydb.cursor()   # create a cursor object using the cursor() method of the connection object

# mycursor.execute("CREATE DATABASE mydatabase")   # execute a sql statement to create a mydatabase database
# mycursor.execute("SHOW DATABASES")   # execute a sql statement to show all databases

# for x in mycursor:   # iterate through the results returned by the cursor
    # print(x)   # print each database name