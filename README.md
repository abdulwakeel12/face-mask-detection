
# Face Mask Detection using CNN

This project uses a **Convolutional Neural Network (CNN)** to detect whether a person is wearing a **face mask** or not from an uploaded image. It leverages the **TensorFlow** library to load a pre-trained model and process images using **Streamlit** for a simple web interface.

## Project Timeline
**June 2025 - June 2025**

---

## Table of Contents
- [Project Overview](#project-overview)
- [Technologies Used](#technologies-used)
- [How It Works](#how-it-works)
- [Installation](#installation)
- [Usage](#usage)
- [License](#license)

## Project Overview

The **Face Mask Detection** app is designed to help detect whether a person is wearing a mask. The app uses a **CNN-based model** that classifies images into two categories: **Mask** and **No Mask**. The app is built using **Streamlit** for the frontend interface, making it interactive and easy to use.

The model is trained using a large dataset of images that have been labeled with either "with mask" or "without mask," and **TensorFlow** is used for the machine learning model.

## Technologies Used

- **Streamlit**: For creating the interactive user interface of the app.
- **TensorFlow**: For building and using the machine learning model to detect masks.
- **NumPy**: For numerical operations and image data processing.
- **Pillow**: For handling image files and processing them before feeding them into the model.

## How It Works

1. **Image Upload**: Users can upload an image (JPEG, PNG, JPG) to the app.
2. **Model Prediction**: Once the image is uploaded, it is resized to 224x224 pixels and normalized before being passed through the pre-trained model.
3. **Prediction Output**: The model predicts whether the person is wearing a **mask** or not and displays the result on the app.

## Installation

To run this app locally, follow the steps below.

### 1. Clone the repository:

```bash
git clone https://github.com/your-username/face-mask-detection.git
```

### 2. Install dependencies:

Create a **virtual environment** (optional but recommended):

```bash
python -m venv venv
```

Activate the virtual environment:

- On **Windows**:
  ```bash
  venv\Scriptsctivate
  ```
- On **macOS/Linux**:
  ```bash
  source venv/bin/activate
  ```

Then install the required dependencies:

```bash
pip install -r requirements.txt
```

## Usage

### Running the App Locally:
To run the app locally, use the following command:

```bash
streamlit run app.py
```

This will start the **Streamlit** server and open the app in your browser.

### Upload an Image:
Once the app is running, click on **"Choose an image..."** to upload an image for mask detection. The model will classify the image as either **Mask** or **No Mask**.
