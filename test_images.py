import torch
from ultralytics import YOLO
import cv2
import os

model = YOLO('best.pt')

source_path = r"C:\Helmet Detect Project\Helmet_Detection_DataSet\test\images"

output_path = r"C:\Helmet Detect Project\output"

results = model.predict(
    source=source_path,
    conf = 0.5,
    project = output_path,
    name = "Predicted Images",
    save=True
)
 
print("Detect Completed")
print(f"Result saved to: {os.path.join(output_path, 'Predicted Images')}")
