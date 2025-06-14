# 🧠 Brain Tumor Detection Application

This is a Streamlit-based web application for detecting brain tumors in MRI images using YOLOv5 object detection model.

## Features

- Upload MRI images (supports JPG, JPEG, PNG formats)
- Real-time tumor detection and classification
- Visual display of detection results
- Confidence scores for predictions
- User-friendly interface

## Prerequisites

- Python 3.9 or higher
- pip (Python package installer)
- Anaconda (recommended for environment management)

## Installation

1. Clone this repository:
```bash
git clone <repository-url>
cd brain-tumor-app
```

2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

The application requires the following packages:
- streamlit
- torch
- torchvision
- Pillow
- opencv-python

## Usage

1. Start the application:
```bash
streamlit run app.py
```

2. Open your web browser and navigate to:
   - Local URL: http://localhost:8501
   - Network URL: http://<your-ip>:8501

3. Upload an MRI image using the file uploader

4. View the detection results:
   - Original image
   - Detected tumor with bounding box
   - Tumor type and confidence score

## Model Information

The application uses a custom-trained YOLOv5 model (`best.pt`) for brain tumor detection. The model is loaded using PyTorch Hub and is optimized for medical imaging analysis.

## Project Structure

```
brain-tumor-app/
├── app.py              # Main Streamlit application
├── best.pt            # Trained YOLOv5 model
├── requirements.txt   # Python dependencies
└── README.md         # Project documentation
```

## Performance Optimization

For better performance, you can install the Watchdog module:
```bash
xcode-select --install
pip install watchdog
```

## Notes

- The application is optimized for Apple Silicon (ARM64) architecture
- Make sure you have sufficient disk space for temporary files
- The application automatically cleans up temporary files after each detection

## Troubleshooting

If you encounter any issues:

1. Architecture Compatibility:
   - For Apple Silicon (M1/M2) Macs, ensure you have the ARM64 version of OpenCV:
   ```bash
   pip uninstall opencv-python
   pip install opencv-python
   ```

2. Model Loading:
   - If the model fails to load, ensure you have a stable internet connection
   - The model will be downloaded from PyTorch Hub on first run

3. Memory Issues:
   - Close other memory-intensive applications
   - Ensure you have sufficient RAM available

## License

[Add your license information here]

## Contributing

[Add contribution guidelines here]

## Contact

[Add your contact information here] 