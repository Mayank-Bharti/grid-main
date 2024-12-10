import React, { useState } from 'react';
import axios from 'axios';

const API_CONFIG = {
  Freshness: { url: 'http://127.0.0.1:7000/predict', key: 'file' },
  OCR: { url: 'http://192.168.115.101:7000/upload', key: 'image' },
  Quantity: { url: 'http://127.0.0.1:5000/count', key: 'file' },
};

const ImageUpload = ({ selectedOption, onResult }) => {
  const [uploadedImage, setUploadedImage] = useState(null);

  // Handle image file selection
  const handleImageUpload = (e) => {
    const file = e.target.files[0];
    if (!file) {
      console.error('No file selected');
      return;
    }

    const imageUrl = URL.createObjectURL(file);
    setUploadedImage(imageUrl);

    // Process the uploaded image based on the selected option
    processImage(file);
  };

  // Function to process the image upload request
  const processImage = async (file) => {
    const config = API_CONFIG[selectedOption];
    if (!config) {
      console.error(`Invalid option: ${selectedOption}`);
      onResult([{ label: 'Error', value: 'Invalid option selected' }]);
      return;
    }

    const formData = new FormData();
    formData.append(config.key, file);

    try {
      const response = await axios.post(config.url, formData, {
        headers: { 'Content-Type': 'multipart/form-data' },
      });

      // Process the response based on the selected option
      switch (selectedOption) {
        case 'Freshness':
          handleFreshnessResponse(response);
          break;
        case 'OCR':
          handleOCRResponse(response);
          break;
        case 'Quantity':
          handleQuantityResponse(response);
          break;
        default:
          console.error('Unknown option');
          onResult([{ label: 'Error', value: 'Unknown option' }]);
      }
    } catch (error) {
      console.error('Error processing image:', error);
      onResult([{ label: 'Error', value: error.message || 'Unknown error occurred' }]);
    }
  };

  // Handle response for freshness prediction
  const handleFreshnessResponse = (response) => {
    const prediction = response.data.prediction || 'No prediction received';
    onResult([{ label: 'Freshness Prediction', value: prediction }]);
  };

  // Handle OCR response to extract text from the image
  const handleOCRResponse = (response) => {
    const extractedText = response.data.extracted_text || 'No text extracted';
    const resultArray = parseExtractedText(extractedText);
    onResult(resultArray);
  };

  // Handle response for quantity detection (count items)
  const handleQuantityResponse = (response) => {
    const detections = response.data.detections || [];
    const counts = detections.reduce((acc, detection) => {
      const { class: className } = detection;
      acc[className] = (acc[className] || 0) + 1;
      return acc;
    }, {});

    // Format the results to display as count per item
    const formattedData = Object.keys(counts).map((itemName) => ({
      itemName,
      count: counts[itemName],
    }));
    onResult(formattedData);
  };

  // Parse the extracted text from OCR
  const parseExtractedText = (text) => {
    const lines = text.split('\n').filter((line) => line.trim() !== '');
    return lines.map((line, index) => {
      const [label, value] = line.split(':').map((part) => part.trim());
      return { label: label || `Line ${index + 1}`, value: value || line };
    });
  };

  return (
    <div className="image-upload">
      <h2>{selectedOption} - Upload an Image</h2>
      <input type="file" accept="image/*" onChange={handleImageUpload} />
      {uploadedImage && <img src={uploadedImage} alt="Uploaded" className="uploaded-image" />}
    </div>
  );
};

export default ImageUpload;
