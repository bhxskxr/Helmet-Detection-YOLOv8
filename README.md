# Helmet-Detection-YOLOv8

# 🪖 Bike Helmet Detection System using YOLOv8

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![YOLOv8](https://img.shields.io/badge/YOLOv8-Ultralytics-green)
![OpenCV](https://img.shields.io/badge/OpenCV-ComputerVision-red)
![Status](https://img.shields.io/badge/Status-Completed-success)

---

## 📌 Project Overview

The **Bike Helmet Detection System** is an AI-powered computer vision project that detects whether a person is wearing a helmet or not using **YOLOv8 object detection**.

This system supports:

* 🖼️ Image Detection
* 🎬 Video Processing
* 📷 Real-time Webcam Detection via GUI

It is designed for **traffic monitoring and safety enforcement systems**.

---

## 🚀 Features

✔ Real-time helmet detection
✔ GUI-based application using Tkinter
✔ Video & image processing support
✔ Live violation tracking
✔ Optimized performance (high FPS processing)
✔ Clean and interactive UI

---

## 🧠 Model Details

* Model: YOLOv8 (Ultralytics)
* Classes:

  * `with_helmet`
  * `without_helmet`

📊 Dataset used:
👉 https://universe.roboflow.com/lavanya-f4fhr/bike-helmet-detection-6pxyk

---

## 🛠️ Tech Stack

* **Programming Language:** Python
* **Deep Learning:** YOLOv8 (Ultralytics)
* **Computer Vision:** OpenCV
* **GUI:** Tkinter
* **Libraries:** NumPy, Pillow, Torch

---

## ⚙️ How This Project Was Built

1. Collected dataset from Roboflow
2. Trained YOLOv8 model on custom dataset
3. Exported trained model (`best.pt`)
4. Built:

   * Image detection pipeline
   * Video detection pipeline
   * Real-time webcam detection
5. Developed GUI interface using Tkinter
6. Optimized performance for real-time processing

---

## 📂 Project Structure

```bash
Helmet-Detection-YOLOv8/
│── detect_video.py
│── test_images.py
│── test_model.py
│── gui.py
│── best.pt
│── requirements.txt
│── README.md
```

---

## ⚙️ Installation

### 1️⃣ Clone Repository

```bash
git clone https://github.com/your-username/Helmet-Detection-YOLOv8.git
cd Helmet-Detection-YOLOv8
```

---

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ How to Run

### 🔹 Test Model

```bash
python test_model.py
```

### 🔹 Run Image Detection

```bash
python test_images.py
```

### 🔹 Run Video Detection

```bash
python detect_video.py
```

### 🔹 Launch GUI Application

```bash
python gui.py
```

---

## 📊 Output

* Annotated images/videos with bounding boxes
* Detection Labels:

  * 🔴 No Helmet
  * 🟢 Helmet

---

## 📈 Future Improvements

* License Plate Recognition
* Cloud Deployment (AWS/GCP)
* Mobile App Integration
* Multi-object tracking
