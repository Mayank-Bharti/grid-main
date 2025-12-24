from pymongo import MongoClient
import os

MONGO_URI = os.getenv(
    "MONGO_URI",
    "mongodb+srv://MAYANKBHARTI:%231Mayank@cluster0.cuuaksv.mongodb.net/hackathonDB?retryWrites=true&w=majority"
)

def get_db():
    client = MongoClient(MONGO_URI)
    return client["hackathonDB"]

db = get_db()
print("MongoDB Atlas connected successfully!")
