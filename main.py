from ultralytics import YOLO

# Load a model from scratch
model = YOLO("yolov8n.yaml")

# Train the model
results = model.train(data="capy.yaml", epochs=1,device="mps", project="runs/detect/")

# Validate on training data
model.val()