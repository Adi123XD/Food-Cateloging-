# import streamlit as st
# from PIL import Image
# import os
# import tempfile
# import requests
# from io import BytesIO
# import pandas as pd
# from main import *
# from mongo import *

# # Streamlit app interface
# st.title("HealthKart Food Label Cataloging")
# uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png", "webp"])
# image_url = st.text_input("Or enter an image URL...")

# def download_and_save_image(url):
#     response = requests.get(url, verify=False)
#     image = Image.open(BytesIO(response.content))
#     with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as temp_file:
#         image.save(temp_file, format="JPEG")
#         return temp_file.name

# def load_image(image_path):
#     image = Image.open(image_path)
#     image = image.convert("RGB")
#     return image

# if uploaded_file or image_url:
#     # Clear previous data (optional)
#     st.empty()

#     if uploaded_file:
#         # Display the uploaded image
#         image = load_image(uploaded_file)
#         st.image(image, caption='Uploaded Image', use_column_width=True)
#         with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as temp_file:
#             image.save(temp_file, format="JPEG")
#             temp_path = temp_file.name
#     elif image_url:
#         try:
#             # Download, save, and display the image from URL
#             temp_path = download_and_save_image(image_url)
#             image = load_image(temp_path)
#             st.image(image, caption='Image from URL', use_column_width=True)
#         except Exception as e:
#             st.error(f"Error loading image from URL: {e}")
#             temp_path = None

#     if temp_path:
#         # Save the downloaded image for inspection
#         st.write(f"Saved image path: {temp_path}")

#         # Perform OCR
#         with st.spinner('Detecting text...'):
#             detected_text = detect_text(temp_path)
#             cleaned_text = clean_ocr_text(detected_text)
#             st.write("Detected Text:")
#             st.write(detected_text)
#             output = extract_nutrients(cleaned_text)
#             output["original_image_link"]=image_url

#         # Convert the dictionary to a pandas DataFrame
#         df = pd.DataFrame(list(output.items()), columns=['Nutrient', 'Value'])
        
#         # Display the extracted text
#         st.write("Detected Nutrients:")

#         # Display the DataFrame as a table using Streamlit 
#         st.table(df)
#         st.write(f'This food is {healthy_unhealthy(cleaned_text)} for you')
        
#         try:
#             skip_entry = all(value == "0.0 g" for value in output.values())
#             if not skip_entry:
#                 insert_to_db(output, "HealthKart", "Food Catalogs")
#                 st.write("Data Inserted successfully")
#             else:
#                 st.error("Image was too blurry")
#         except Exception as e:
#             st.error(f"An error occurred: {e}")

#         # Clean up temporary file
#         os.remove(temp_path)
import streamlit as st
from PIL import Image
import os
import tempfile
import requests
from io import BytesIO
import pandas as pd
from main import *
from mongo import *

# Streamlit app interface
st.title("HealthKart Food Label Cataloging")
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png", "webp"])
# Add two text inputs for the URLs
image_url_to_process = st.text_input("Enter the image URL for processing...")
image_url_to_store = st.text_input("Enter the image URL to store in the database...")

# Add a button to trigger the processing
if st.button("Enter"):
    def download_and_save_image(url):
        response = requests.get(url, verify=False)
        image = Image.open(BytesIO(response.content))
        with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as temp_file:
            image.save(temp_file, format="JPEG")
            return temp_file.name

    def load_image(image_path):
        image = Image.open(image_path)
        image = image.convert("RGB")
        return image

    if image_url_to_process and image_url_to_store:
        try:
            # Download, save, and display the image from the URL to process
            temp_path = download_and_save_image(image_url_to_process)
            image = load_image(temp_path)
            st.image(image, caption='Image for Processing', use_column_width=True)
            response = requests.get(image_url_to_store, verify=False)
            image_display = Image.open(BytesIO(response.content))
            st.image(image=image_display, use_column_width=True)
        except Exception as e:
            st.error(f"Error loading image from URL to process: {e}")
            temp_path = None

        if temp_path:
            # Save the downloaded image for inspection
            st.write(f"Saved image path: {temp_path}")

            # Perform OCR
            with st.spinner('Detecting text...'):
                detected_text = detect_text(temp_path)
                cleaned_text = clean_ocr_text(detected_text)
                st.write("Detected Text:")
                st.write(cleaned_text)
                output = extract_nutrients(cleaned_text)
                output["original_image_link"] = image_url_to_store  # Use the URL to store in the database
                # Check for serving size and adjust nutrient values
                serving_size_text = output.get("weight", "0.0 g")
                serving_size = float(serving_size_text.split()[0])
                if serving_size > 0:
                    output = adjust_nutrient_values(output, serving_size)
            output = format_data(output)
            output['healthType']=healthy_unhealthy(cleaned_text)
            # Convert the dictionary to a pandas DataFrame
            df = pd.DataFrame(list(output.items()), columns=['Nutrient', 'Value'])
            # Display the extracted text
            st.write("Detected Nutrients:")

            # Display the DataFrame as a table using Streamlit 
            st.table(df)
            # st.write(f'This food is {healthy_unhealthy(filtered_df)} for you')
            
            try:
                skip_entry = all(value == "0.0 g" for value in output.values())
                if not skip_entry:
                    insert_to_db(output, "HealthKart", "Food Catalogs")
                    st.write("Data Inserted successfully")
                else:
                    st.error("Image was too blurry")
            except Exception as e:
                st.error(f"An error occurred: {e}")

            # Clean up temporary file
            os.remove(temp_path)
    elif uploaded_file:
        image = load_image(uploaded_file)
        st.image(image, caption='Uploaded Image', use_column_width=True)
        with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as temp_file:
            image.save(temp_file, format="JPEG")
            temp_path = temp_file.name
        if temp_path:
            # Save the downloaded image for inspection
            st.write(f"Saved image path: {temp_path}")

            # Perform OCR
            with st.spinner('Detecting text...'):
                detected_text = detect_text(temp_path)
                cleaned_text = clean_ocr_text(detected_text)
                st.write("Detected Text:")
                st.write(cleaned_text)
                output = extract_nutrients(cleaned_text)
                output["original_image_link"] = image_url_to_store  # Use the URL to store in the database
                # Check for serving size and adjust nutrient values
                serving_size_text = output.get("weight", "0.0 g")
                st.write(serving_size_text)
                serving_size = float(serving_size_text.split()[0])
                if serving_size > 0:
                    output = adjust_nutrient_values(output, serving_size)
            output = format_data(output)
            output['healthType']=healthy_unhealthy(cleaned_text)
            # Convert the dictionary to a pandas DataFrame
            df = pd.DataFrame(list(output.items()), columns=['Nutrient', 'Value'])
            # Display the extracted text
            st.write("Detected Nutrients:")

            # Display the DataFrame as a table using Streamlit 
            st.table(df)
            # st.write(f'This food is {output['healthType']} for you')
            
            try:
                skip_entry = all(value == "0.0 g" for value in output.values())
                if not skip_entry:
                    insert_to_db(output, "HealthKart", "Food Catalogs")
                    st.write("Data Inserted successfully")
                else:
                    st.error("Image was too blurry")
            except Exception as e:
                st.error(f"An error occurred: {e}")

            # Clean up temporary file
            os.remove(temp_path)
        st.error("Please enter both URLs.")
