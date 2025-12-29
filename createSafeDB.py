import mysql.connector   #import sql.connector module

dass = mysql.connector.connect(   #establish a connection to the mysql database
    host = "localhost",   #specify the host
    user = "root",   # specify the user name
    password = "root"   #specify the password
)

cursor = dass.cursor()   # create the cursor object using the cursor() method of the connection object

cursor.execute("CREATE DATABASE IF NOT EXISTS safe_database")   # execute a sql statement to create database in safe mode and named safe_database
print("database created successully")   # print database create successfully if the database createdsuccessfully

cursor.execute("SHOW DATABASES")   # execute a sql statement to show all database 

for db in cursor:  # iterate through the results returned by the cursor
    print(db)   # print all database names