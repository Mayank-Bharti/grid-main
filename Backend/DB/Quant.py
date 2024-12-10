from DB.connect import db
from datetime import datetime

def store_quantity_result(image_name, detections):
    collection = db['quantity']
    result = {
        "image_name": image_name,
        "detections": detections,
        "timestamp": datetime.now()
    }
    collection.insert_one(result)
