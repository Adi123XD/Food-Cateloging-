import streamlit as st
from PIL import Image
import os
import tempfile
from main import *

# Streamlit app interface
st.title("HealthKart Food Label Cataloging")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Display the uploaded image
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image', use_column_width=True)
    
    # Save the uploaded image to a temporary file
    with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as temp_file:
        image.save(temp_file, format="JPEG")
        temp_path = temp_file.name
    
    # Perform OCR
    with st.spinner('Detecting text...'):
        detected_text = detect_text(temp_path)
        output = generate_gemini_content(detected_text)
    
    # Display the extracted text
    st.write("Detected Nutrients :")
    st.text(output)
    
    # Clean up temporary file
    os.remove(temp_path)