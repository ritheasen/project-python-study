
#importing the driver into the python code
import mysql.connector

#establishing connection and storing the connection into a variable
connection = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "ritheasen@root15032003", #ritheasen@root15032003
    port = "3306"
)

#creating cursor
cursor = connection.cursor()

#write query to creat databse

cursor.execute("CREATE DATABASE kit")
print("Datbase created successfully...")