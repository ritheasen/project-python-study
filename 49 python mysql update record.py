import mysql.connector

connection = mysql.connector.connect(
    host = "localhost",
    port = "3306",
    user = "root",
    password = "ritheasen@root15032003",
    database = "kit"


)

cursor = connection.cursor()
sidToUpdate = int(input("Input the sid of the record to be updated:"))
snameToUpdate = input("Input the updated name:")
cursor.execute(f"UPDATE dse10 SET sname = '{snameToUpdate}' WHERE sid = {sidToUpdate}")

print("Successfully record updated")

connection.commit()