import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image, ImageOps

# Load the trained model
@st.cache_resource
def load_model():
    model = tf.keras.models.load_model("brain_tumor_model.h5")
    return model

model = load_model()

# Class labels
CLASS_NAMES = ["Glioma", "Meningioma", "No Tumor", "Pituitary"]

# Function to preprocess the uploaded image
def preprocess_image(image):
    """Ensure proper image formatting before feeding into the model."""
    
    # Convert image to RGB (handles grayscale and non-RGB formats)
    if image.mode != "RGB":
        image = image.convert("RGB")
    
    # Resize while maintaining aspect ratio (Use LANCZOS instead of ANTIALIAS)
    target_size = (299, 299)
    image = ImageOps.fit(image, target_size, Image.LANCZOS)
    
    # Convert to NumPy array and normalize
    image = np.array(image) / 255.0  
    
    #correct format for the model (batch_size, height, width, channels)
    if len(image.shape) == 2:  # If grayscale, convert to RGB
        image = np.stack((image,) * 3, axis=-1)
    
    image = np.expand_dims(image, axis=0)  # Add batch dimension

    return image

# Streamlit UI
st.set_page_config(page_title="Brain Tumor Detection", page_icon="🧠", layout="centered")

st.markdown(
    """
    <style>
    .big-title { font-size: 40px !important; text-align: center; font-weight: bold; color: #ff4b4b; }
    .subtitle { text-align: center; font-size: 18px; color: #4f8bf9; }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown('<p class="big-title">🧠 Brain Tumor Detection</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Upload an MRI scan to classify it into one of four categories.</p>', unsafe_allow_html=True)

# File uploader
uploaded_file = st.file_uploader("📤 Upload an MRI Image", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    
    # Display the uploaded image
    st.image(image, caption="🖼 Uploaded MRI Image", width=350)

    # Preprocess the image
    processed_image = preprocess_image(image)

    # Print shape for debugging
    st.write(f"✅ Processed Image Shape: {processed_image.shape}")

    # Make prediction
    predictions = model.predict(processed_image)
    predicted_class = CLASS_NAMES[np.argmax(predictions)]
    confidence = np.max(predictions) * 100  # Confidence score

    # Display prediction
    st.success(f"🎯 Prediction: **{predicted_class.upper()}**")
    st.info(f"🔍 Confidence: {confidence:.2f}%")

    # Show probability distribution as a horizontal bar chart
    st.subheader("📊 Prediction Confidence Scores")
    st.bar_chart({CLASS_NAMES[i]: predictions[0][i] for i in range(len(CLASS_NAMES))})
