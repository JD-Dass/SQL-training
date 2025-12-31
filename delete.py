#  delete data from table

import mysql.connector

dass = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "root",
    database = "expense_tracker3"
)

mycursor = dass.cursor()

sql = "DELETE FROM expenses WHERE id = %s"   #deleted data from exepenses
id = (5,)

mycursor.execute(sql, id)

dass.commit()

print(mycursor.rowcount, "record(s) deleted")