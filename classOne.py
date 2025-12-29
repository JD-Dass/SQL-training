import mysql.connector

dass = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "root"
)

print(dass)