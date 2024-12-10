from flask import Flask, request, jsonify
import cv2
import pytesseract
import re
from datetime import datetime
from flask_cors import CORS
from DB.connect import db  # Import MongoDB connection
from DB.descript import store_ocr_result  # Import the function to store results in DB

app = Flask(__name__)
CORS(app, origins=["http://localhost:3000"])  # Only allow requests from this origin

# Specify the Tesseract command path
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Function to extract expiry date using regex
def extract_expiry_date(text):
    patterns = [
        r'(\d{2}[/-]\d{2}[/-]\d{4})',       # Format: DD/MM/YYYY or DD-MM-YYYY
        r'(\d{2}[/-]\d{4})',                # Format: MM/YYYY
        r'\b(Best Before|Use By|Expires On|Exp\. Date|Expiry Date)\b.*?(\d{2}[/-]\d{2}[/-]\d{4})',
        r'\b(Best Before|Use By|Expires On|Exp\. Date|Expiry Date)\b.*?(\d{2}[/-]\d{4})'
    ]
    for pattern in patterns:
        match = re.search(pattern, text, re.IGNORECASE)
        if match:
            return match.group(0)  # Return the first matching expiry date
    return "Not Found"  # Return if no expiry date is found

# Function to classify expiry status
def check_expiry_status(expiry_date):
    try:
        # Parse expiry date into datetime
        if "-" in expiry_date:
            date_format = "%d-%m-%Y" if len(expiry_date) > 7 else "%m-%Y"
        elif "/" in expiry_date:
            date_format = "%d/%m/%Y" if len(expiry_date) > 7 else "%m/%Y"
        else:
            return "Invalid Date Format", "gray"

        exp_date = datetime.strptime(expiry_date, date_format)
        today = datetime.now()
        days_left = (exp_date - today).days

        if days_left < 0:
            return "Expired", "red"
        elif days_left <= 7:
            return "Near Expiry", "orange"
        else:
            return "Fresh", "green"
    except Exception as e:
        return "Error in Date Parsing", "gray"

@app.route('/upload', methods=['POST'])
def upload_image():
    if 'image' not in request.files:
        return jsonify({"error": "No image uploaded"}), 400

    file = request.files['image']
    image_name = file.filename
    file.save("temp_image.jpg")

    # Read the saved image using OpenCV
    img = cv2.imread("temp_image.jpg")
    
    # Convert image to grayscale
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # Apply Gaussian Blur to reduce noise
    blurred_img = cv2.GaussianBlur(gray_img, (5, 5), 0)
    
    # Use Otsu's Thresholding for better contrast
    _, thresholded_img = cv2.threshold(blurred_img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    # Use pytesseract to extract text with custom config for better accuracy
    custom_config = r'--oem 3 --psm 6'  # OEM 3 (Default), PSM 6 (Assume a single block of text)
    text = pytesseract.image_to_string(thresholded_img, config=custom_config)

    # Extract expiry date
    expiry_date = extract_expiry_date(text)

    # Check expiry status
    status, color = check_expiry_status(expiry_date)

    # Store the results in MongoDB using the existing function
    store_ocr_result(image_name, text, expiry_date, status, color)

    # Return the result as a JSON response
    return jsonify({
        "extracted_text": text,
        "expiry_date": expiry_date,
        "expiry_status": status,
        "status_color": color
    })

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=7000)
