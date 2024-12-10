from DB.connect import db
from datetime import datetime

def store_ocr_result(image_name, extracted_text, expiry_date, status, color):
    collection = db['ocr']  # Your MongoDB collection for OCR results
    result = {
        "image_name": image_name,
        "extracted_text": extracted_text,
        "expiry_date": expiry_date,
        "expiry_status": status,
        "status_color": color,
        "timestamp": datetime.now()
    }
    collection.insert_one(result)
