# UPDATE data from table

import mysql.connector

dass = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "root",
    database = "expense_tracker3"
)

mycursor = dass.cursor()

sql = "UPDATE expenses SET amount = 100, category = 'medical', note = 'for mom' WHERE id = 1;"    #update data from the spesific column using WHERE clause

mycursor.execute(sql)

dass.commit()

print(mycursor.rowcount, "record(s) updated")