## SQL 
1. Define a database : an organized collection of data stored and accessed electronically through the use of a 
database management system(system software for creating and managing database)

- RDBMS  (sql) - related /relation - mysql(postgresql, mysqlconnect) - sqlite -  - microsoft sql server 

- NewSQL DBMS / NRDBMS / (nosql) - non-relation - CockroachDB - Volt Active Data - 
NOSQL ( Google Firebase(HTML ,CSS , JS)) (MongoDB)

2. Know what the sqlite : embedded database management system included in an application 
sqlite3 / sqlite

3. How to set up sqlite for use withing python app / sql queries command / adding an sqlite viewer

4. CRUD operations (SQL fundamentals)
5. a simple Python CRUD sqlite app. 


## SQL Fundamentals 
1. What is SQL : Structured Query Language : standard language for accessing and manipulating databases 
<!-- catalogue of popular sql commands / weekly focus commands  -->
 - Select 
 - Update 
 - Delete 
 - Insert into 
 - create database 
 - alter database 
 - create table 
 - alter table 
 - drop table : deletes a table 
 - create index 
 - drop index 

 - Structure of a table : rows (records) and columns (specific fields for each record.)
 - CRUD : todays focus 


 ## Table Relationships in SQL 
 how tables are related or connected to each other within a database. 

 ## How to Establish relationships between tables : 
- Through keys : a. Once column in one table correspond 
                 b. to another column(s) in another table

- The keys should be unique in all the tables (PRIMARY KEY)
- Keys establish connections between rows in different tables , allowing for efficient and structured data 
management. 

## Tasks db 
## tasks table, users table 
## Form a relationship between the users and the tasks allocations 

## Different types of relationships 
1. One to Many relationship (Task to User) : each task can be associated with only one user , but each user can be associated multiple tasks. 

### to achieve this type of relationship 
add a FORIENG KEY in the tasks table that references the id column in the users table 
id  , name , description , user_id (value of the user_id field will be the id value in the users table)

by doing this , each task now belongs to (belongsTo) a specific user ()


2. Many to Many relationship (Users and Tasks)

