from ultralytics import YOLO
model = YOLO('runs/train/food_detection_model/weights/best.pt')
def detect_food(image_path):
    results = model.predict(source=image_path, conf=0.25)
    return results