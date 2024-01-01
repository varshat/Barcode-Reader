from ultralytics import YOLO
import os
# Load a model
model = YOLO('./runs/detect/train/weights/best.pt')  # build a new model from scratch  

# get the path/directory
folder_dir = "./data/test imgs"

# Run inference on the source
model.predict(source=folder_dir,save=True,save_crop=True)