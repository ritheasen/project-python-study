import mysql.connector

conection = mysql.connector.connect(
    host = " localhost",
    port = "3306",
    user = "root",
    password = "ritheasen@root15032003",
    database = "kit"
)

cursor = conection.cursor()
cursor.execute("INSERT INTO dse10 VALUES (%s, %s, %s);",(1234,"Panha",20))

print("Record inserted successfully")

conection.commit()