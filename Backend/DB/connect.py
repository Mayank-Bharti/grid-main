from pymongo import MongoClient
import os

def get_db():
    client = MongoClient(os.getenv("MONGO_URI", "mongodb://localhost:27017"))
    db = client['hackathonDB']  # Replace with your desired database name
    return db

db = get_db()

# Check if the db object is not None
if db is not None:
    print("MongoDB connected successfully!")
else:
    print("Failed to connect to MongoDB")
