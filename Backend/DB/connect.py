from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()  # Load .env file

MONGO_URI = os.getenv("MONGO_URI")  # Get URI from environment

def get_db():
    client = MongoClient(MONGO_URI)
    return client["hackathonDB"]

db = get_db()
print("MongoDB connected successfully!")
