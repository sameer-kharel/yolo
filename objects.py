
import os
os.environ['KMP_DUPLICATE_LIB_OK']='True'

from ultralytics import YOLO

# Load a pretrainied yolov8n model
model = YOLO("yolov8m.pt")

# to open tha camera
results = model.track(source=0, show=True, tracker="bytetrack.yaml")

