# python -m venv yolov8_env
# yolov8_env\Scripts\activate
# pip install ultralytics
# python -c "from ultralytics import YOLO; print('Ultralytics installed successfully!')"
# pip install opencv-python matplotlib
#1) Open VS Code: Navigate to the folder where your Python project resides.

#2) Install Python Extension: Install the official Python extension for VS Code:

#3) Go to the Extensions view (Ctrl+Shift+X or Cmd+Shift+X on Mac).
# 4)Search for "Python" and install it.
#5) Select Python Interpreter:

# a)Press Ctrl+Shift+P (or Cmd+Shift+P on Mac).
# b)Type and select Python: Select Interpreter.
# c)Choose your virtual environment (e.g., yolov8_env).
# d)activate virtual invironment and run python file (python count.py)=> python -m venv yolov8_env


from flask import Flask, request, jsonify
import os
import cv2
from ultralytics import YOLO
from werkzeug.utils import secure_filename
from flask_cors import CORS
from DB.Quant import store_quantity_result   # Import the function from the utility module
from datetime import datetime

app = Flask(__name__)

# Configure CORS
CORS(app, resources={r"/count": {"origins": "http://localhost:3000"}})

# Load the pretrained YOLOv8 model
model = YOLO('C:\\Users\\bhart\\OneDrive\\Documents\\GitHub\\grid-main\\Backend\\yolov8n.pt')

# Define allowed file types
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'webp'}
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/count', methods=['POST'])
def count_items():
    try:
        # Check if the file is part of the request
        if 'file' not in request.files:
            return jsonify({'error': 'No file part'}), 400

        file = request.files['file']

        if file.filename == '':
            return jsonify({'error': 'No selected file'}), 400

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)

            try:
                # Load the image using OpenCV
                image = cv2.imread(file_path)

                # Perform inference with YOLOv8
                results = model(image)

                # Process results
                detections = []
                object_counts = {}  # Dictionary to store counts of each object

                for result in results:
                    for box in result.boxes:
                        class_id = int(box.cls)  # Class ID
                        class_name = model.names[class_id]  # Class Name
                        confidence = float(box.conf[0])  # Confidence score
                        x1, y1, x2, y2 = map(int, box.xyxy[0])  # Bounding box coordinates

                        # Add detection to the list
                        detections.append({
                            'class': class_name,
                            'confidence': confidence,
                            'box': [x1, y1, x2, y2]
                        })

                        # Count the object occurrences
                        if class_name in object_counts:
                            object_counts[class_name] += 1
                        else:
                            object_counts[class_name] = 1

                # Store the detection result in the MongoDB database using the utility function
                store_quantity_result(filename, detections)

                # Return both detections and object counts
                return jsonify({
                    'detections': detections,
                    'object_counts': object_counts
                }), 200
            finally:
                # Clean up uploaded file
                os.remove(file_path)
        else:
            return jsonify({'error': 'Invalid file type'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
