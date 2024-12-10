# import torch
# print(torch.__version__)
# print(torch.cuda.is_available())  # Check if CUDA is available
# from ultralytics import YOLO
# print("Ultralytics imported successfully!")

from DB.freshness import store_freshness_result

# Example image name and prediction
image_name = "apple_image.jpg"
prediction = "Apple(1-5)"

# Call the function to store the result in MongoDB
store_freshness_result(image_name, prediction)
