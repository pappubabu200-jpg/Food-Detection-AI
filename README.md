# Food Detection AI
YOLOv8-based food detection model for mobile apps.

# Food Detection AI

## Overview
A YOLOv8-based food detection AI system designed for mobile apps.
- Detects 200+ food classes
- Integrates with USDA API for nutrition information
- Provides training, inference, and visualization pipelines
- Fully production-ready for mobile or web integration

## Features
- **Automated Food Detection:** Detects multiple food items per image
- **Nutrition Integration:** Fetches nutrition data from USDA API
- **Real-Time Inference:** Fast and accurate detection (<2s per image)
- **Mobile App Ready:** Backend can be integrated with Flutter (Android/iOS)
- **Extensible:** Easily add new food classes or datasets

## Folder Structure
food-detection-ai/
├── README.md
├── prerequisites.md
├── .gitignore
├── config/
│   └── api_keys_placeholder.txt
├── datasets/
│   ├── raw/
│   ├── annotated/
│   └── augmented/
├── backend/
│   ├── main.py
│   ├── model_train.py
│   ├── model_inference.py
│   ├── data_loader.py
│   └── nutrition_api.py
├── frontend/
│   ├── demo_app.py
│   └── ui_placeholder.py
├── utils/
│   ├── augmentation.py
│   ├── evaluation.py
│   └── visualization.py
├── logs/
└── docs/
    ├── project_overview.md
    └── deployment_instructions.md

  ## setup
  pip install torch torchvision ultralytics opencv-python requests
 ## Set up API keys:



# config/api_keys_placeholder.txt
USDA_API_KEY=your_usda_api_key_here

## Prepare datasets:



Place raw images in datasets/raw/

Annotate using YOLO format and place in datasets/annotated/

Data augmentation results go to datasets/augmented/

## Training

python backend/model_train.py

Trains YOLOv8 model

Saves best model to runs/train/food_detection_mod

## Inference

python backend/model_inference.py

Detect food items in an image

Returns bounding boxes, class IDs, and confidence

## Demo App

python frontend/demo_app.py

Runs a demo showing detection and nutrition info

Uses utils/visualization.py to draw bounding boxes
