from pymongo import MongoClient
import datetime

uri = "CONNECTION_STRING"
client = MongoClient(uri)

database = client["test_database"]
collection = database["test_collection"]

post = {
    "author": "Anjal Bhattarai",
    "text": "My first blog post!",
    "tags": ["mongodb", "python", "pymongo"],
    "date": datetime.datetime.now()
}
post_id = collection.insert_one(post).inserted_id
