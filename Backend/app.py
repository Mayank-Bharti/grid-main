# C:\\Users\\Mayank bharti\\Documents\\GitHub\\grid\\Backend\\model_final1

import torch
from flask import Flask, request, jsonify
from PIL import Image
import numpy as np
import io
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS to allow cross-origin requests

# Load your trained model
model_path = 'C:\\Users\\Mayank bharti\\Documents\\GitHub\\grid\\Backend\\model_final1'  # Adjust to your model path
model = torch.load(model_path, map_location=torch.device('cpu'))  # Load the model for CPU
model.eval()  # Set model to evaluation mode

# Define your class labels
class_labels = [
    'Apple(1-5)', 'Apple(10-14)', 'Apple(5-10)',
    'Banana(1-5)', 'Banana(10-15)', 'Banana(15-20)', 'Banana(5-10)',
    'Carrot(1-2)', 'Carrot(3-4)', 'Expired',
    'Tomato(1-5)', 'Tomato(10-15)', 'Tomato(5-10)', 'carrot(5-6)'
]

# Preprocess function
def preprocess_image(image_bytes):
    """Preprocess image data for prediction (adapt as per your training requirements)."""
    img = Image.open(io.BytesIO(image_bytes))
    img = img.resize((224, 224))  # Resize as per your model input size
    img = np.array(img).astype(np.float32) / 255.0  # Normalize image
    img = np.transpose(img, (2, 0, 1))  # Convert to channels-first
    img = torch.tensor(img).unsqueeze(0)  # Add batch dimension
    return img

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400

    file = request.files['file']
    img_bytes = file.read()

    # Preprocess the image
    img = preprocess_image(img_bytes)

    # Make the prediction
    with torch.no_grad():
        outputs = model(img)
        _, predicted_class = torch.max(outputs, 1)  # Get predicted class

    # Return the prediction result based on your class labels
    prediction = class_labels[predicted_class.item()]

    # Return the prediction result
    return jsonify({'prediction': prediction})

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)
