# import sqlite3 package 
import sqlite3

# first we need to create the database 
# variable to create a reference to a connection to our db 
conn = sqlite3.connect('moringa.db')

# Databases -> tables 
# CREATE DBNAME;
# CREATE TABLE : command used to create a db table 
# makeup : tablename , columns(fields of the table) , attributes of the fields (columns)
# db : students / tms : students  : id :datatype, extrainfo(auto increment) 
#  , name: TEXT, NOT NULL  , email: TEXT, NULL
# to make my relational models each record should have a unique field (PRIMARY KEY)
# to execute the command we pair our connection with .execute method. 
conn.execute('''CREATE TABLE IF NOT EXISTS students(
                     id INTEGER PRIMARY KEY,
                     name TEXT NOT NULL, 
                     email TEXT NULL
            );''')

# tms;
conn.execute('''CREATE TABLE IF NOT EXISTS tms(
                     id INTEGER PRIMARY KEY,
                     name TEXT NOT NULL, 
                     email TEXT NULL,
                     staffnumber INTEGER NOT NULL
            );''')

# CRUD 
# students table 
name = "joseph mbugua"
email = "joseph.mbugua@moringaschool.com"
# TO create a record we use the command : INSERT INTO tablename()
# when inserting we use a technique called Prepared Statements (placeholders)
# 
conn.execute("INSERT INTO students (name,email) VALUES (?,?)", (name, email))
conn.execute("INSERT INTO students (name,email) VALUES (?,?)", ("Mary", "mary@gmail.com"))

# Read : SELECT columns1,columns2 FROM tablename
# SELECT * FROM tablename
# sequence (List)
result = conn.execute("SELECT * FROM students")
# loop to see data 
for row in result:
    print(f"id : {row[0]}, Name: {row[1]} , Email: {row[2]} ")

# Update  : UPDATE tablename SET fieldname = ? , fieldname = ? WHERE id = ?" , (values)
conn.execute("UPDATE students SET name = ? WHERE id = ?", ("Bill",1))
# Delete : DELETE FROM tablename 
#  DELETE FROM tablename WHERE id = ? , (values)
conn.execute("DELETE FROM students WHERE id = ?", (2,))
# commit changes to our db
conn.commit()
# close the connection 
conn.close()














