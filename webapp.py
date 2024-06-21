import streamlit as st
from PIL import Image
import os
import tempfile
from main import *
from mongo import *

# Streamlit app interface
healthy =""
st.title("HealthKart Food Label Cataloging")

st.text_input("Product Name ...")
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
  # Clear previous data (optional)
  st.empty()

  # Display the uploaded image
  image = Image.open(uploaded_file)
  st.image(image, caption='Uploaded Image', use_column_width=True)
  # Convert the image to RGB mode
  image = image.convert("RGB")
  
  # Save the uploaded image to a temporary file
  with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as temp_file:
    image.save(temp_file, format="JPEG")
    temp_path = temp_file.name
    # st.write(temp_path)
  
  # Perform OCR
  with st.spinner('Detecting text...'):
    detected_text = detect_text(temp_path)
    cleaned_text = clean_ocr_text(detected_text)
    # if(healthy_unhealthy(cleaned_text)):
    #   healthy="healthy"
    # else:
    #   healthy="unhealthy"     
    # cleaned_text = clean_with_gemini(detected_text)
    st.write(detected_text)
    output = extract_nutrients(detected_text)
  # Convert the dictionary to a pandas DataFrame
  df = pd.DataFrame(list(output.items()), columns=['Nutrient', 'Value'])
  # Display the extracted text
  st.write("Detected Nutrients :")

  # Display the DataFrame as a table using Streamlit 
  st.table(df)
  st.write(f'This food is {healthy_unhealthy(cleaned_text)} for you')
  try:
      skip_entry = all(value =="0.0 g" for value in output.values())
      if (not skip_entry):
          insert_to_db(output, "HealthKart" , "Food Catelogs")
          st.write("Data Inserted successfully")
      else:
          st.error("Image was too blurry")  
  except Exception as e:
    print(f"An Error occured {e}")
    st.error(e)
  
  # Clean up temporary file
  os.remove(temp_path)
