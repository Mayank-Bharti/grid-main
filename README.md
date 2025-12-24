# Smart Vision Technology Quality Control

### Automating the quality and quantity testing process for India's largest ecommerce platform using smart vision technology.

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Technology Stack](#technology-stack)
- [Installation](#installation)
- [Video](#video)
- [Screenshots](#screenshots)

---

## Introduction
This project is a smart vision-based quality testing system designed for the ecommerce industry. The system automates the inspection of products, ensuring both quality and quantity control using *high-resolution cameras, **image processing, and **deep learning*. It significantly reduces manual labor, improves accuracy, and offers real-time defect detection.

## Features
- *OCR (Optical Character Recognition)*: Extracts product information, brand, expiration date, and MRP from product labels.
- *Freshness Detection*: Analyzes visual cues to assess the freshness of perishable goods.
- *Quantity Detection*: Automatically counts products, ensuring that correct quantities are packed and shipped.

## Technology Stack
- *Frontend*:
  
  - React.js
  - CSS
    
- *Backend*:
  
  - Node.js
  - Python Flask
    
- *Deep Learning*:
  
  - TensorFlow for CNN (Convolutional Neural Networks)
  - Tesseract.js for OCR
  - Pytorch
  - Keras
  - OpenCV
  - easyOCR
    
- *Hardware*:
  
  - High-resolution cameras for image capture

## Installation
To run this project locally, follow these steps:

1. *Clone the repository*:
   bash
   git clone https://github.com/Mayank-Bharti/grid-main.git
   cd grid-main
2. *Install frontend dependencies*:
   bash
   cd ./frontend                                                                                                                                                                                    cd frontend
   npm install
   npm run dev
4. *Install backend dependencies*:
   bash
   cd ./backend
   For Quantity: 1.python -m venv yolov8_env
                 2. yolov8_env\Scripts\activate
                 3. pip install ultralytics, pip install opencv-python matplotlib, pip install flask flask-cors, pip install pytesseract, pip install pymongo, pip install load_dotenv
                 4. Run `python count.py`
   For OCR: 1. Install all dependencies like pip install flask flask-cors pymongo opencv-python pytesseract load_dotenv
            2.Download Tesseract OCR: https://github.com/tesseract-ocr/tesseract
            3. Install it in your system.
            4. Add in environment variables path,[C:\Program Files\Tesseract-OCR\]
            5. Add in code [pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe']
            6. Run `python ocr.py`
   For app.py: 1. Install all dependencies like pip install flask flask-cors pymongo opencv-python torch load_dotenv
               2. Run `python app.py`

6. *Access the backend application*:
    ### Freshness: `[http://127.0.0.1:7000/predict]`
    ###  OCR: `[http://127.0.0.1:7001/upload]`
    ### Quantity: `[http://127.0.0.1:5000/count]`
7. *Access the Frontend application*:
   ### Navigate to `[http://localhost:5173]`

## Video
### [[Click to see the working here:]](https://drive.google.com/file/d/16wsj61l5UNGWje-TKSJ9a00oofQB8RsK/view?usp=drive_link)

## Screenshots
![Screenshot 2024-10-21 000143](https://github.com/user-attachments/assets/12987f41-6ac7-4a97-95ad-0050386acf0a)
![Screenshot 2024-10-21 000200](https://github.com/user-attachments/assets/1d57c81c-a9fb-4045-b1ab-3ce826ed365a)
![Screenshot 2024-10-21 000307](https://github.com/user-attachments/assets/6a9b0f77-d638-4fbe-b56a-f43c33fb43d0)
![Screenshot 2024-10-21 000341](https://github.com/user-attachments/assets/3826adef-bc8e-4232-bd65-4223eecd3b3d)
![Screenshot 2024-10-21 000410](https://github.com/user-attachments/assets/e50bf909-b0e7-4db8-a4b1-eed689ad6e34)

## Contact
### If you have any doubts or suggestions you can always reach out to me from the ways mentioned below:
- Email: `mayankbharti349@gmail.com`
- GitHub: `https://github.com/Mayank-Bharti/`
- LinkedIn: `www.linkedin.com/in/mayank-bharti-839b07261`
