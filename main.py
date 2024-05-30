import os, io,re
from google.cloud import vision,vision_v1
from google.cloud.vision_v1 import types
from importlib.resources import path
import pandas as pd
from constants import *
import google.generativeai as genai
from dotenv import load_dotenv
load_dotenv()


# load the model
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel("gemini-pro")

os.environ["GOOGLE_APPLICATION_CREDENTIALS"]=r'healthkart-catelogging-57eaebe5246c.json'

client = vision.ImageAnnotatorClient()

def clean_with_gemini(ocr_text):
    prompt =f'''This is the ocr_text {ocr_text}
    i want you to clean this text and correct all the spellings and return the paragraph'''
    response = model.generate_content(prompt)
    return response.text
def clean_ocr_text(ocr_text):
    # Remove non-informative lines and whitespace
    lines = ocr_text.split('\n')
    cleaned_lines = []
    for line in lines:
        if line.strip() and not re.match(r'^\d+\s*$', line):
            cleaned_lines.append(line.strip())
    return " ".join(cleaned_lines)

def extract_nutrients(text):
  # Define regular expressions for different nutrients

    extracted_nutrients = {}
    for nutrient, pattern in nutrient_patterns.items():
        match = re.search(pattern, text, re.IGNORECASE)
        if match:
            #   #print("matched ",nutrient)
            value=None 
            unit =None
            flag =0
            #print("matched", nutrient , match.groups())
            for i, group in enumerate(match.groups(), start=1):
                #print(nutrient , group)
                if group:
                    if group.replace('.', '', 1).isdigit() and flag==0:
                        value = float(group)
                        #print(nutrient , "value = ",value, unit)
                        flag =1
                    elif ( group.lower()=='o'):
                        value =0
                        #print(nutrient , "value = ",value, unit)
                    elif group.lower()=='l':
                        value =1
                        #print(nutrient , "value = ",value, unit)
                    elif group in ['g', 'mg', 'mcg','mog','µg']:
                        unit = group
                        #print(nutrient , "value = ",value, unit)
                    elif group in ['%']:
                        #print(nutrient , "value = ",value, unit,end=" ")
                        value=None
                        #print(nutrient , "value = ",value, unit)
                        continue
            if (unit is None and value is not None and (int(value)%10==9 or int(value)%10 ==0) and value==int(value)):
                unit ='g'
                #print(nutrient , "value = ",value, unit) 
                value= str(int(value)//10)
            if (unit=="mg"):
                #print(nutrient,"initial value ",value ,end=" ")
                value = value/1000
                #print("new value ",value)
                unit ="g"
            elif unit =="mcg" or unit =="mog" or unit =='µg':
                #print(nutrient,"initial value", value,end=" ")
                value= value/1000000
                #print("new value",value)
                unit ="g"
            elif unit is None :
                unit = 'g'
            if value is not None :
                #print("before adding the data ",nutrient, value , unit )
                extracted_nutrients[nutrient] = f"{value} {unit}"
    for incorrect_nutrient, correct_nutrient in nutrient_correction.items():
        if incorrect_nutrient in extracted_nutrients:
            # If the incorrect nutrient is found, replace it with the correct one
            extracted_nutrients[correct_nutrient] = extracted_nutrients.pop(incorrect_nutrient)
    for nutrient in nutrients:
        if nutrient not in extracted_nutrients:
            extracted_nutrients[nutrient] = "0.0 g"
    return extracted_nutrients

def detect_text(img_path):
    with io.open(img_path,"rb") as image_file:
        content = image_file.read()
    image = vision_v1.types.Image(content = content)
    response = client.text_detection(image=image)
    texts=response.text_annotations
    output =""
    for text in texts:
        output=output+ text.description
    return output

# # Example usage
# ocr_text = detect_text(r"data\label3.jpg")
# # #print("OCR Text Output:\n", ocr_text)  # #print the raw OCR text output for inspection

# cleaned_text = clean_ocr_text(ocr_text)
# #print("\nCleaned Text:\n", cleaned_text)  # #print the cleaned text for inspection
# #print(extract_nutrients(cleaned_text))



    