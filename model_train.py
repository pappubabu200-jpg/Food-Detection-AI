from ultralytics import YOLO
model = YOLO('yolov8n.pt')
model.train(data='datasets/food_dataset.yaml', epochs=50)