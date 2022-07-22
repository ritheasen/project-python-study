import pymongo

client = pymongo.MongoClient("mongodb://127.0.0.1:27017/") #client is important
newDB = client["firsttest"] #if it doesnt exist it will create new db#can use .<name>

newCollection = newDB.testing #creating collection .<name> inside db

#create record to insert in collection
record = {
            "id" : 1,
            "name":"Bala",
            "sex":"M",
            "age":1
            }

record1 = {
            "id" : 2,
            "name":"Pablo",
            "sex":"M",
            "age":12
            }
record2 = {
            "id" : 3,
            "name":"Mahee",
            "sex":"F",
            "age":13
            }
record3 = [{
            "id" : 4,
            "name":"Kake",
            "sex":"M",
            "age":15   
            },
            {
            "id" : 5,
            "name":"Pwel",
            "sex":"F",
            "age":16   
            },
            {
            "id" : 6,
            "name":"Samba",
            "sex":"M",
            "age":17  
            }
]
#method to insert
#newCollection.insert_one(record)
#newCollection.insert_many([record1,record2])
newCollection.insert_many(record3)
#newCollection.insert_many([record1,record2,record3])

cursor = newCollection.find()
for recordd in cursor:
    print(recordd)


