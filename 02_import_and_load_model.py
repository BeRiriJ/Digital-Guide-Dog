from ultralytics import YOLO
# !pip install ultralytics

# Load a model
# model = YOLO("yolov8n.yaml")  # build a new model from scratch
model = YOLO("yolov8n.pt")  # load a pretrained model (recommended for training)
source = '02_source_image.jpg'
# results = model(source=source, show=True, conf=0.1, save=True, device='mps')
results = model.predict(source=source, show=True, conf=0.1, save=True, project='runs', name='detect')
print(results)
