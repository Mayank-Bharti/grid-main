// components/ImageUpload.js
import React, { useState } from 'react';
import axios from 'axios'; // Import axios for making HTTP requests

const ImageUpload = ({ selectedOption, onResult }) => {
  const [uploadedImage, setUploadedImage] = useState(null);

  const handleImageUpload = (e) => {
    const file = e.target.files[0];
    const imageUrl = URL.createObjectURL(file);
    setUploadedImage(imageUrl);
    
    // Call the API with the uploaded image
    processImage(file);
  };

  const processImage = async (file) => {
    const formData = new FormData();
  
    // Append the file or image based on the selected option
    switch (selectedOption) {
      case 'Freshness':
        formData.append('file', file); // Use 'file' key for Freshness
        break;
      case 'OCR':
        formData.append('image', file); // Use 'image' key for OCR
        break;
      case 'Quantity':
        // Simulating a response for the Quantity option
        setTimeout(() => {
          const Data = [
            { itemName: 'Banana', count: 3 },
          ];
          onResult(Data); // Pass the dummy data to the onResult function
        }, 1000); // Simulate network delay
        return; // Return early since we don't call an API for Quantity
      default:
        console.error('Invalid option selected');
        return;
    }
  
    let apiUrl;
  
    // Set the API URL based on the selected option
    switch (selectedOption) {
      case 'Freshness':
        apiUrl = 'http://127.0.0.1:5000/predict';
        break;
      case 'OCR':
        apiUrl = 'http://192.168.83.129:5000/upload'; // Ensure this is correct
        break;
        case 'Quantity':
  // Simulating a response for the Quantity option
  setTimeout(() => {
    const Data = [
      { itemName: 'Banana', count: 3 },
    ];
    onResult(Data); // Pass the dummy data to the onResult function
  }, 1000); // Simulate network delay
      default:
        console.error('Invalid option selected');
        return;
    }
  
    try {
      // Make the API call to your Flask backend
      const response = await axios.post(apiUrl, formData, {
        headers: {
          'Content-Type': 'multipart/form-data', // Set the content type to form data
        },
      });

      // Handle the Freshness response
      if (selectedOption === 'Freshness') {
        if (response.data.prediction) {
          const prediction = response.data.prediction;

          // Process freshness prediction based on the logic provided
          let freshnessResult;
          if (prediction === 'Expired') {
            freshnessResult = 'Expired';
          } else {
            // Extract days from the prediction
            const daysMatch = prediction.match(/\((\d+)-(\d+)\)/);
            if (daysMatch) {
              const minDays = parseInt(daysMatch[1], 10);
              const maxDays = parseInt(daysMatch[2], 10);

              if (minDays >= 10) {
                freshnessResult = `${prediction} - About to Expire`;
              } else {
                freshnessResult = `${prediction} - Fresh`;
              }
            } else {
              freshnessResult = prediction; // Fallback if no specific format is found
            }
          }

          // Pass the processed freshness result to the onResult function
          onResult([{ label: 'Freshness Prediction', value: freshnessResult }]);
        } else {
          console.error('Freshness result is not in the expected format:', response.data);
          onResult('Unexpected result format from Freshness');
        }
      }

      // Handle the OCR response
      if (selectedOption === 'OCR') {
        if (response.data.extracted_text) {
          const extractedText = response.data.extracted_text;

          // Parse the extracted text
          const resultArray = parseExtractedText(extractedText);
          onResult(resultArray); // Pass the formatted array to the onResult function
        } else {
          console.error('OCR result is not in the expected format:', response.data);
          onResult('Unexpected result format from OCR');
        }
      }
    } catch (error) {
      console.error('Error uploading image:', error);
      onResult('Error uploading image'); // Handle errors gracefully
    }
  };

  // Function to parse the extracted text into an array of objects for OCR
  const parseExtractedText = (text) => {
    const lines = text.split('\n').filter(line => line.trim() !== '');
    const resultArray = [];

    lines.forEach((line, index) => {
      const [label, value] = line.split(':').map(part => part.trim());
      if (value) {
        resultArray.push({ label: label || `Line ${index + 1}`, value });
      } else {
        resultArray.push({ label: `Line ${index + 1}`, value: line }); // Handle lines without key-value
      }
    });

    return resultArray;
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
