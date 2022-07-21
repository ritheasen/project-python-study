import mysql.connector

connection = mysql.connector.connect(
    host = "localhost",
    port = "3306",
    user = "root",
    password = "ritheasen@root15032003",
    database = "kit"


)

cursor = connection.cursor()
sidToDelete = int(input("Input the sid of the record to be deleted:"))
cursor.execute(f"DELETE FROM dse10 WHERE sid = {sidToDelete}")

connection.commit()

