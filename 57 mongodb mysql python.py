
import mysql.connector
import pymongo


client = pymongo.MongoClient("mongodb://127.0.0.1:27017/") 

newDB = client["dse10TEST"] 
newCollection = newDB.dse10 

connection = mysql.connector.connect(
    host = "localhost",
    port = "3306",
    user = "root",
    password = "ritheasen@root15032003",
    database = "kit"
)

cursor = connection.cursor(dictionary = True)


cursor.execute(f"SELECT * FROM dse10" )

students = cursor.fetchall()

if len(students) > 0:
    sqlToMongo = newCollection.insert_many(students)
    print(len(sqlToMongo.inserted_ids))




