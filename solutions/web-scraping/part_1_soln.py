from pymongo import MongoClient

client = MongoClient('localhost', 27017)
# Access/Initiate Database
db = client['test_database']
# Access/Initiate Table
test_collection = db['test_collection']

#insert a document into the collection
test_collection.insert_one({"this_is_the_field":"this_is_the_value"})

#let's see what's in the collection
for doc in test_collection.find():
    print(doc)
    
#update the record
test_collection.update_one({"this_is_the_field":"this_is_the_value"}, {"$set": {"this_is_the_field":"this_is_the_new_value"}})

#now take a look
for t in test_collection.find():
    print(doc)
    
