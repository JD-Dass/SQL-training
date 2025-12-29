import mysql.connector

dass = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "root",
    database = "expense_tracker"
)

mycursor = dass.cursor()

mycursor.execute("ALTER TABLE expenses ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY FIRST")   
#add a primary key column named id to the expenses table
print("primary key added successfully")