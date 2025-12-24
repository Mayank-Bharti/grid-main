from DB.connect import db
from datetime import datetime

def store_freshness_result(image_name, prediction):
    collection = db['freshness']  # Cloud MongoDB collection
    result = {
        "image_name": image_name,
        "prediction": prediction,
        "timestamp": datetime.now()
    }
    collection.insert_one(result)
    print("Freshness result stored in MongoDB Atlas!")
