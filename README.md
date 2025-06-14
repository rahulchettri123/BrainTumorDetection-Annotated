# 🧠 Brain Tumor Detection Using YOLOv5 and Streamlit

This project presents an end-to-end solution for **brain tumor detection** in MRI images using a custom-trained **YOLOv5 object detection** model. It includes steps for data annotation, model training, and a web-based inference app built with **Streamlit**.

## 📌 Project Highlights

- Custom annotations using **LabelImg**
- Object detection with **YOLOv5**
- Real-time tumor classification and bounding boxes
- **Streamlit app** for interactive MRI analysis
- Classes supported: `glioma`, `meningioma`, `pituitary`, `notumor`

## 🗂️ Folder Structure

```
brain-tumor-detection/
├── dataset/
│   ├── images/
│   │   ├── train/ # Training images
│   │   └── val/   # Validation images
│   ├── labels/
│   │   ├── train/ # YOLO-format labels
│   │   └── val/
│   └── data.yaml  # Dataset config
├── yolov5/        # YOLOv5 repo (cloned)
├── runs/          # Training outputs
├── brain-tumor-app/ # Streamlit app
│   ├── app.py
│   ├── best.pt
│   └── requirements.txt
└── README.md      # This file
```

## 🧪 Dataset and Annotation

- MRI images organized by class: `glioma`, `meningioma`, `pituitary`, `notumor`
- Annotated using **LabelImg**
- Bounding boxes saved in YOLOv5 format (`.txt`)
- Split into **train** and **val** sets
- Configured with `data.yaml` for YOLOv5

## 🧠 Model Training (YOLOv5)

1. Clone YOLOv5 repo:
```bash
git clone https://github.com/ultralytics/yolov5
cd yolov5
pip install -r requirements.txt
```

2. Train the model:
```bash
python train.py --img 640 --batch 16 --epochs 50 \
    --data ../dataset/data.yaml --weights yolov5s.pt --name tumor-detect
```

Final weights saved at:
```
runs/train/tumor-detect/weights/best.pt
```

## 🚀 Streamlit Web App

An easy-to-use UI to upload MRI images and detect brain tumors in real time.

### 🔧 Installation

```bash
cd brain-tumor-app
pip install -r requirements.txt
```

### ▶️ Run App

```bash
streamlit run app.py
```

Local: http://localhost:8501

Upload image → Get prediction + bounding box + class + confidence

## 📈 Model Performance

| Metric        | Validation Set |
|---------------|----------------|
| mAP@0.5      | 0.92          |
| mAP@0.5:0.95 | 0.68          |
| Precision     | 0.94          |
| Recall        | 0.91          |

## 🛠 Tech Stack

- Python 3.9+
- PyTorch
- YOLOv5
- LabelImg
- OpenCV
- Streamlit

## 📝 Notes

- Optimized for Apple Silicon (ARM64)
- Use LabelImg for bounding box annotation in training & testing sets
- Clean-up logic in Streamlit app ensures no leftover files

## 📬 Contact

Created by Rahul Chettri
- rahulchettri601@gmail.com
- https://www.linkedin.com/in/rahulchettri123/



[![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://www.python.org)
[![YOLOv5](https://img.shields.io/badge/YOLOv5-v5.0-green.svg)](https://github.com/ultralytics/yolov5)
[![Streamlit](https://img.shields.io/badge/Streamlit-v1.31.1-red.svg)](https://streamlit.io)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE) 
