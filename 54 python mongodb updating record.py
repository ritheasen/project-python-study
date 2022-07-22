import pymongo

client = pymongo.MongoClient("mongodb://127.0.0.1:27017/") #client is important
newDB = client["firsttest"] #if it doesnt exist it will create new db#can use .<name>

newCollection = newDB.testing #creating collection .<name> inside db



#newUpdate = newCollection.update_one({"id": 5},{"$set":{"name":"Kala"}})

newUpdateMany = newCollection.update_many({"sex":"M"},{"$set":{"sex":"F"}})



