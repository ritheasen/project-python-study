import pymongo

client = pymongo.MongoClient("mongodb://127.0.0.1:27017/") #client is important
newDB = input("Enter database name") 
#if it doesnt exist it will create new db#can use .<name>
print(f"client.{newDB}")

newCollection = input("Enter collection name") 
#creating collection .<name> inside db
print(f"newDB.{newCollection}")


#create record to insert in collection

#method to insert
#newCollection.insert_many(record3)
#newCollection.insert_many([record1,record2,record3])




