from pymongo import MongoClient
import os

client  = MongoClient(os.getenv("MONGO_URI", "mongodb://localhost:27017/"))
db = client["conversational_ai"]

users_col = db["users"]
sessions_col = db["sessions"]
messages_col = db["messages"]
products_col = db["products"]