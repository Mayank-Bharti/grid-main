from flask import Flask, request, jsonify
import cv2
import pytesseract
from flask_cors import CORS


app = Flask(__name__)
CORS(app, origins=["http://localhost:3000"])  # Only allow requests from this origin


# Specify the Tesseract command path
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

@app.route('/upload', methods=['POST'])
def upload_image():
    if 'image' not in request.files:
        return jsonify({"error": "No image uploaded"}), 400
    
    file = request.files['image']
    file.save("temp_image.jpg")

    # Read the saved image using OpenCV
    img = cv2.imread("temp_image.jpg")
    
    # Use pytesseract to extract text
    text = pytesseract.image_to_string(img)

    return jsonify({"extracted_text": text})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
