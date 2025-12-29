import mysql.connector

dass = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "root",
    database = "expense_tracker"  # specify the database name
)

print("connected to expense_tracker database successfully")