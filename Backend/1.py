import torch
print(torch.__version__)
print(torch.cuda.is_available())  # Check if CUDA is available
from ultralytics import YOLO
print("Ultralytics imported successfully!")

