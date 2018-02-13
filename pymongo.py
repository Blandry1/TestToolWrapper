# import datetime
# post = {"author": "Mike",
#         "text": "My first blog post!",
#         "tags": ["mongodb", "python", "pymongo"],
#         "date": datetime.datetime.utcnow()
#         } # a json document

import pymongo
#from pymongo import MongoClient
#client = MongoClient('localhost', 27017) # connects client with the mongoserver

# db = client.test_database # create a database

# collection = db.test_collection # create a collection

# posts = db.posts # create a posts collection
# post_id = posts.insert_one(post).inserted_id  # insert a document into a collection
# post_id

# db.collection_names(include_system_collections=False) # list all collection 

#import pprint
#pprint.pprint(posts.find_one({"author": "Mike"}))
