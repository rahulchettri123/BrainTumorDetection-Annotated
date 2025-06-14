🧠 Brain Tumor Detection Using YOLOv5 and Streamlit
This project presents an end-to-end pipeline for detecting brain tumors (glioma, meningioma, pituitary, or no tumor) in MRI scans using a custom-trained YOLOv5 object detection model. The solution includes data annotation, model training, and deployment via a Streamlit web application.

📌 Project Highlights
Annotated and labeled bounding boxes using LabelImg

Trained custom YOLOv5 model on annotated MRI data

Achieved high detection accuracy across 4 tumor types

Built an interactive Streamlit app for real-time predictions

🗂️ Folder Structure

brain-tumor-detection/
├── dataset/
│   ├── images/
│   │   ├── train/         # Training images
│   │   └── val/           # Validation images
│   ├── labels/
│   │   ├── train/         # YOLO-format bounding boxes
│   │   └── val/
│   └── data.yaml          # Dataset config for YOLOv5
├── runs/                  # YOLOv5 training outputs
├── yolov5/                # YOLOv5 repo (cloned from Ultralytics)
├── brain-tumor-app/       # Streamlit app folder
│   ├── app.py
│   ├── best.pt
│   └── requirements.txt
└── README.md              # Project documentation
🧪 Dataset and Annotation
Dataset includes MRI scans of four classes:

glioma

meningioma

pituitary

notumor

Annotation was performed using LabelImg

Bounding boxes were saved in YOLOv5 format (.txt)

Split into training and validation sets

🧠 Model Training (YOLOv5)
Clone the YOLOv5 repo:

bash
Copy
Edit
git clone https://github.com/ultralytics/yolov5
cd yolov5
pip install -r requirements.txt
Train the model:

bash
Copy
Edit
python train.py --img 640 --batch 16 --epochs 50 --data ../dataset/data.yaml --weights yolov5s.pt --name tumor-detect
Output will be saved to runs/train/tumor-detect/

🚀 Streamlit Web App
A lightweight web UI to upload and analyze MRI images using the trained YOLOv5 model.

🔧 Setup & Run
bash
Copy
Edit
cd brain-tumor-app
pip install -r requirements.txt
streamlit run app.py
Then open: http://localhost:8501

🖼️ Sample Results
<p align="center"> <img src="assets/sample1.jpg" width="45%"> <img src="assets/sample2.jpg" width="45%"> </p>
📈 Model Performance
Metric	Validation Set
mAP@0.5	0.92
mAP@0.5:0.95	0.68
Precision	0.94
Recall	0.91

🛠 Tech Stack
Python 3.9+

YOLOv5

PyTorch

LabelImg

Streamlit

OpenCV & Pillow


📬 Contact
Created by Rahul Chettri
