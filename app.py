import streamlit as st
import tensorflow as tf
from tensorflow.keras.preprocessing import image
import numpy as np
from PIL import Image

# Load the trained model (replace with the correct path to your model)
model = tf.keras.models.load_model('face_mask_detection_model.h5')

# Function to predict mask or no mask
def predict_mask(img):
    img = img.resize((224, 224))  # Resize the image to match model input size
    img_array = np.array(img) / 255.0  # Normalize pixel values
    img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension
    prediction = model.predict(img_array)
    return 'Mask' if prediction[0] > 0.5 else ' No Mask'

# Streamlit UI
st.title("Face Mask Detection App By Abdul Wakeel")
st.markdown("Upload an image to detect whether the person is wearing a mask.")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    img = Image.open(uploaded_file)
    st.image(img, caption='Uploaded Image', use_column_width=True)
    st.write("")
    label = predict_mask(img)
    st.write(f"Prediction: **{label}**")