import mysql.connector

#establishing connection and storing the connection into a variable
connection = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "ritheasen@root15032003",
    port = "3306",
    database = "kit"
)

cursor = connection.cursor()
cursor.execute("CREATE TABLE dse10 ( sid INT(3), sname VARCHAR(50), age INT(2))")


print("Table dse10 created successfully under kit table")
cursor.execute("DESCRIBE dse10;")

result = cursor.fetchall()

for res in result:
    print(res)