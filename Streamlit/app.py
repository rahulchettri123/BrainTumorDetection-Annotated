import streamlit as st
import torch
from PIL import Image
import os
import shutil

# Load YOLOv5 model
@st.cache_resource
def load_model():
    return torch.hub.load('ultralytics/yolov5', 'custom', path='best.pt', force_reload=True)

model = load_model()

# Streamlit UI
st.title("🧠 Brain Tumor Detection")
st.write("Upload an MRI image to detect the tumor type and location.")

uploaded_file = st.file_uploader("Upload MRI image", type=["jpg", "jpeg", "png"])

if uploaded_file:
    img = Image.open(uploaded_file).convert('RGB')
    img_path = "input.jpg"
    img.save(img_path)

    st.image(img, caption="Uploaded MRI", use_column_width=True)

    # Run detection
    results = model(img_path)
    results.save()

    # Display result
    output_path = os.path.join("runs", "detect", "exp", "input.jpg")
    if os.path.exists(output_path):
        st.image(output_path, caption="Detected Tumor", use_column_width=True)
        st.success("Prediction complete!")
        st.write(results.pandas().xyxy[0][['name', 'confidence']])
    else:
        st.error("No detection made.")

    # Cleanup for rerun
    if os.path.exists("runs"):
        shutil.rmtree("runs")
