# 🚗 Carcounting

![Python](https://img.shields.io/badge/python-3.8%2B-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Status](https://img.shields.io/badge/status-active-brightgreen.svg)

A computer vision project that counts the number of automobiles passing through a defined detection line in a video stream. This system utilizes OpenCV for background subtraction, object detection, and tracking to provide a real-time count of vehicles.

🌐 **GitHub Repository**: You're here!

## Table of Contents
- [Features](#-features)
- [Tech Stack](#️-tech-stack)
- [Installation](#️-installation)
- [Usage](#-usage)
- [How it Works](#-how-it-works)
- [License](#-license)

## 🌟 Features
- **Automated Vehicle Counting**: Counts vehicles in a video feed as they cross a designated line.
- **Background Subtraction**: Employs MOG (Mixture of Gaussians) for robust background subtraction to isolate moving objects.
- **Object Detection**: Identifies vehicles using contour detection and filtering based on size (minimum width and height).
- **Vehicle Tracking**: Tracks detected objects and increments a counter when they cross a predefined line.

## 🛠️ Tech Stack
- **Python**: 3.8+
- **Computer Vision**: OpenCV (`cv2`)
- **Numerical Operations**: NumPy
- **Data Manipulation**: Pandas

## ⚙️ Installation
1.  Clone the repository:
    ```bash
    git clone [https://github.com/maithil06/carcounting.git](https://github.com/maithil06/carcounting.git)
    cd carcounting
    ```
2.  Create a virtual environment (optional but recommended):
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```
3.  Install dependencies:
    ```bash
    pip install opencv-python numpy pandas
    ```

## 🚀 Usage
1.  Place your input video file (e.g., `video.mp4`) in the root directory of the project.
2.  Run the Jupyter Notebook:
    ```bash
    jupyter notebook "Car counting.ipynb"
    ```
    Or execute the Python script (if converted from the notebook):
    ```bash
    python "Car counting.py"
    ```
3.  The script will open a window displaying the video feed with detected vehicles and the real-time count.
4.  Press `Enter` to exit the video playback.

## 🧠 How it Works
The system processes each frame of the video:
1.  **Grayscale Conversion & Blur**: Frames are converted to grayscale and blurred to reduce noise.
2.  **Background Subtraction**: The `createBackgroundSubtractorMOG()` algorithm is applied to extract foreground objects (vehicles).
3.  **Morphological Operations**: Dilation and morphological closing operations are applied to enhance the detected moving objects and fill gaps.
4.  **Contour Detection**: Contours are found around the foreground objects, representing potential vehicles.
5.  **Filtering & Bounding Boxes**: Contours are filtered based on `min_width` (80) and `min_height` (80) to identify actual vehicles. Bounding boxes are drawn around these vehicles.
6.  **Centroid Calculation**: The center point of each detected vehicle is calculated.
7.  **Vehicle Counting**: A horizontal line is drawn across the video frame at `count` (550). When the centroid of a detected vehicle crosses this line within a small `offset` (6), the `counter` is incremented, and the vehicle is removed from the `detect` list to avoid double-counting.

## 📜 License
This project is licensed under the MIT License. See the repository for details.
