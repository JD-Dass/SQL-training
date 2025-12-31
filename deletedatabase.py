# DELETE DATABASE

import mysql.connector

dass = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "root",
)

mycursor = dass.cursor()

mycursor.execute("DROP DATABASE IF EXISTS expense_tracker")

print("database deleted successfully!")