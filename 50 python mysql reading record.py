import mysql.connector

connection = mysql.connector.connect(
    host = "localhost",
    port = "3306",
    user = "root",
    password = "ritheasen@root15032003",
    database = "kit"


)

cursor = connection.cursor()

cursor.execute("SELECT * FROM dse10")

students = cursor.fetchall()


for student in students:
    print(f"sid: {student[0]},sname: '{student[1]}',sage: {student[2]}")



