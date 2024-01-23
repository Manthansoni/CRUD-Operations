# Importing module
import mysql.connector

# Creating connection object
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="bacancytask"
)

# Printing the connection object
print(mydb)

cursor = mydb.cursor()

# For creating Database
# cursor.execute("CREATE DATABASE BacancyTask")

# ----------------------------------------------------------------------------

# For Showing Database
# cursor.execute("SHOW DATABASE")

# for x in cursor:
#     print(x)

# To See all TABLES

# cursor.execute("SHOW TABLES")

# for x in cursor:
#     print(x)

# ----------------------------------------------------------------------------

# For creating table
# cursor.execute("CREATE TABLE task1 (id int AUTO_INCREMENT, name VARCHAR(255), field VARCHAR(255), pNum BIGINT, PRIMARY KEY (ID))")

# ----------------------------------------------------------------------------

# For Inserting Data
# qry1 = "INSERT INTO task1 VALUES (' ',%s, %s,%s)"
# val = ("Manthan", "Python", 940)

# cursor.execute(qry1, val)
# mydb.commit()

# print(cursor.rowcount, "details inserted")

# ----------------------------------------------------------------------------

# Update query
# qry2 = "UPDATE task1 SET pNum = 9409205790 WHERE name ='Manthan'"

# cursor.execute(qry2)
# mydb.commit()

# ----------------------------------------------------------------------------

# Select Data
# cursor.execute("Select * from task1")
# myresult = cursor.fetchall()
# for i in myresult:
#     print(i)
