import mysql.connector

dass = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "root",
    database = "expense_tracker" # specify the database name
)

mycursor = dass.cursor()   # create a mycursor object using cursor() method of the connection object

mycursor.execute("CREATE TABLE expenses (date DATE, category VARCHAR(255), amount DECIMAL(10, 2), note TEXT)")   #create a table named expensees with columns date, category, amount, note

print("Table created successfully")   # print table created successfully if created a table

mycursor.execute("SHOW TABLES")  # execute a sql statement to show table 

for table in mycursor:   # iterate through the results returned by the mycursor
    print(table)  # print all table names one by one