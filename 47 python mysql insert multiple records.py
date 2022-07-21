import mysql.connector

connection = mysql.connector.connect(
    host = "localhost",
    port = "3306",
    user = "root",
    password = "ritheasen@root15032003",
    database = "kit"


)



cursor = connection.cursor()

print("Successfulyl connected with the DB")

numOfRecords = int(input("Input number of records to insert:"))
for i in range (numOfRecords):
    sid = int(input("Enter sid:"))
    sname = str(input("Enter sname:"))
    sage = int(input("Enter sage:"))
    cursor.execute(f"INSERT INTO dse10 VALUE ({sid},'{sname}',{sage})")



connection.commit()

print(f"{numOfRecords} records have been stored in dse10...")

print("Input number of records to insert:")