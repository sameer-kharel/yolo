
import os
os.environ['KMP_DUPLICATE_LIB_OK']='True'

from ultralytics import YOLO

# Load a pretrainied yolov8n model
model = YOLO("yolov8m.pt")
# path = " ya chai path hala image ya video ko"



# yo chai camera ko lagi ho camera kholinxa
results = model.track(source=0, show=True, tracker="bytetrack.yaml")



# yo chai path hale si chalau mathi ko ma comment banara 
# results = model.track(source=path, show=True, tracker="bytetrack.yaml")