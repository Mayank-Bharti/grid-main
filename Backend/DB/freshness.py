from DB.connect import db
from datetime import datetime

def store_freshness_result(image_name, prediction):
    # Access the 'freshness' collection from the 'hackathonDB' database
    collection = db['freshness']  # Create a collection for freshness results
    result = {
        "image_name": image_name,
        "prediction": prediction,
        "timestamp": datetime.now()  # Store the timestamp when the data is inserted
    }
    collection.insert_one(result)  # Insert the result document into the collection
    print("Freshness result stored in the database!")
