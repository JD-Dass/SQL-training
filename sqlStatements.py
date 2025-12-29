"""
Document for sql statements

mysql -u root -p    #login to mysql

SHOW DATABASES;   #show all databases

#create table
CREATE DATABASE database_name;   #create a new database

USE database_name;   #use a specific database

CREATE TABLE table_name (
                         heading1 datatype, 
                         heading2 datatype, 
                         heading3 datatype, 
                         etc...
                         );    #create a new table

SHOW TABLES;   #show all tables in the database

DESCRIBE table_name;   #describe the structure of a table
or
DESC table_name;    #describe the structure of a table

#insert data into table
INSERT INTO table_name (
                        heading1, 
                        heading2, 
                        heading3, 
                        etc...
                        )    # insert data into a table
                VALUES (
                        value1, 
                        value2, 
                        value3, 
                        etc...
                        ),
                        (
                        value1, 
                        value2, 
                        value3, 
                        etc...) ;   #insert data into atable

#select data from table
SELECT * FROM table_name;   #select all data from a table

SELECT heading1 FROM table_name;   #select specific column data from a table

SELECT heading1, heading2 FROM table_name;   #select specific columns data from a table

#select data from table with condition
SELECT * FROM table_name WHERE condition;    #select data from a table with a specific condition

#with ordering and limiting results
SELECT * FROM table_name ORDER BY heading1 ASC/DESC;    #select data from a table ordered by a specific column in ascending / descrnding order

SELECT * FROM table_name LIMIT number;   #select limited number of rows from a table

SELECT * FROM table_name ORDER BY heading1 DESC LIMIT  number;   #select limited number of rows from a table ordered by a specific coumn in descending order

#aggregate functions
SELECT COUNT(heading1) FROM table_name;   #count number of rows in a specific column

SELECT SUM(heading1)  FROM table_name;   #sum of all valuves in a specific column

SELECT AVG(heading1) FROM table_name;   #average of all values in a specific colums

SELECT MAX(heading1) FROM table_name;   #maximum value in a specific colums

SELECT MIN(heading1) FROM table_name;   #minimum value in a specific colums

#category wise total
SELECT heading1, SUM(heading2) FROM table_name GROUP BY heading1;   #group by specific column and get sum of another column

#update data in table
UPDATE table_name SET column_name = new_value WHERE condition;   #update data in a table with a specific condition

UPDATE table_name SET column_name = new_value, column_name = new_value, column_name = new_value WHERE condition;  #update multiple column data in a table with a specific condition

#delete data in table
DELETE FROM table_name WHERE condition;   #delete data from the table using WHERE clause

"""
