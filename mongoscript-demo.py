from pymongo import MongoClient
import datetime

uri = "mongodb+srv://anjalbhattarai79_db_user:F5IgTwbGF5LwbLHx@cluster0.7xoowcq.mongodb.net/"
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