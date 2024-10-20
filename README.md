# Smart Vision Quality Testing System

### Automating the quality and quantity testing process for India's largest ecommerce platform using smart vision technology.

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Technology Stack](#technology-stack)
- [Installation](#installation)
- [Usage](#usage)
- [Screenshots](#screenshots)
- [Challenges Faced](#challenges-faced)
- [Future Improvements](#future-improvements)
- [Contributing](#contributing)
- [License](#license)

---

## Introduction
This project is a smart vision-based quality testing system designed for the ecommerce industry. The system automates the inspection of products, ensuring both quality and quantity control using *high-resolution cameras, **image processing, and **machine learning*. It significantly reduces manual labor, improves accuracy, and offers real-time defect detection.

## Features
- *OCR (Optical Character Recognition)*: Extracts product information, brand, expiration date, and MRP from product labels.
- *Freshness Detection*: Analyzes visual cues to assess the freshness of perishable goods.
- *Quantity Detection*: Automatically counts products, ensuring that correct quantities are packed and shipped.
- *Real-Time Feedback*: Provides immediate insights into product quality and alerts for defective items.
- *Automated Integration*: Works seamlessly with conveyor belts and inventory management systems.

## Technology Stack
- *Frontend*: 
  - React.js
  - CSS (Green and Creamish color theme)
- *Backend*:
  - Node.js (Express.js)
  - Flask
- *Machine Learning*:
  - TensorFlow for CNN (Convolutional Neural Networks)
  - Tesseract.js for OCR
- *Hardware*:
  - High-resolution cameras for image capture
  - Lighting control for optimal image quality

## Installation
To run this project locally, follow these steps:

1. *Clone the repository*:
   bash
   git clone https://github.com/your-username/smart-vision-quality-testing.git
   cd smart-vision-quality-testing                                                                                                                                                  2. 2. 2. *Install frontend dependencies*:
   bash                                                                                                                                                                                       cd frontend
   npm install
3. *Install backend dependencies*:
   bash
   cd ../backend
   npm install
