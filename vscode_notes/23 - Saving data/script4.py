# documents in mongodb 
# is sometimes called a document-based atabase because it isn't organized in rows and columns but instead store documents
# a document is stored in a format called BSON (binary json)
# you need to have access to a mongodb server
# free account and instance on mongodb.com
# then you can create a free mongo atlas cluster for experimentation

# be sure to save the username, password and the connection string shown when creating your cluster
# if you want to run mongodb locally, the easies solution is to run a docker instance:
# "docker run -p 27017:27017 mongo"
# pip install pymongo

from pymongo import MongoClient
client = MongoClient(host='.....')
# testing the client with sample document
import datetime
a_document = {'name':'Jane',
              'age':34,
              'interest':['Python','databases','statistics'],
              'date_added': datetime.datetime.now()}
db = client.my_data # select database wchich hasn't been created yet
collection = db.docs # select a collection in the database, also nt created yet
result = collection.find_one() # searches for first item, no exception even if neither collection or database exist yet
# print(db.list_collection_names())
# to store a document use the  collection isnert_one() method, wchich return the uniqe object id
# print(collection.insert_one(a_document)) ObjectId('6884bd3545a057d80fa25aa2'
# print(collection.find_one()) 
from bson.objectid import ObjectId
# print(collection.find_one(ObjectId('6884bd3545a057d80fa25aa2')))

# updating
# collection.update_one({'_id': ObjectId('6884bd3545a057d80fa25aa2')}, {"$set": {"name":"Ann"}})
# updates record according to contents of $set object

# replacing with another object
# collection.replace_one({'_id': ObjectId('6884bd3545a057d80fa25aa2')},{'name':'Maria'})
# replaces record with new object, the record is replace with a shorter record

# deleting
# collection.delete_one({'_id': ObjectId('6884bd3545a057d80fa25aa2')})

# even thorugh record has been deleted and the collection is now empty the collection still exists unless it's specifically dropped
# print(db.list_collection_names())
# collection.drop()
print(db.list_collection_names())
