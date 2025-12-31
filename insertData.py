#insert data in table

import mysql.connector   #import mysql.connector module

dass = mysql.connector.connect(   #establishing the connection
    host = "localhost",   #host name
    user = "root",   #user name
    password = "root",   #password
    database = "expense_tracker3"   #database name
)

mycursor = dass.cursor()   #craeting cursor object

sql  = """   
INSERT INTO expenses (date, category, amount, note) 
VALUES (%s, %s, %s, %s) 
"""    #sql query to insert data into expenses table 

data = ("2025-10-23", "medical", 200.00, "doctor fees" )    #data to be inserted

mycursor.execute(sql, data)   #execuying the sql query
dass.commit()    #commiting the changes to the database

print("print successfully data inserted")   #print success message