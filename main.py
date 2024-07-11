import os, io,re
from google.cloud import vision,vision_v1
from google.cloud.vision_v1 import types
from importlib.resources import path
import pandas as pd
from constants import *
import google.generativeai as genai
from dotenv import load_dotenv
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import string 
load_dotenv()


# load the model
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel("gemini-pro")

# os.environ["GOOGLE_APPLICATION_CREDENTIALS"]=r'healthkart-catelogging-57eaebe5246c.json'
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]=r'healthkart-catelogging-f5f83b608349.json'

client = vision.ImageAnnotatorClient()

def healthy_unhealthy(ocr_text):
    prompt =f'''{ocr_text}
    
    is this food healthy or unhealthy? answer in a single word'''
    response = model.generate_content(prompt)
    return response.text


def adjust_nutrient_values(output,serving_size):
    for key, value in output.items():
        if key not in ["original_image_link","Serving Size"] and isinstance(value, str):
            nutrient_value = float(value.split()[0])
            # unit_value =value.split()[1]
            adjusted_value = nutrient_value * (serving_size / 100)
            output[key] = f"{round(adjusted_value, 2)} "
    return output
    
    
def clean_ocr_text(text):
    # Tokenize the text into words
    tokens = word_tokenize(text)
    
    # Define allowed characters (alphanumeric, spaces, parentheses, and period)
    allowed_chars = set(string.ascii_letters + string.digits + '() .')
    
    # Remove punctuation and special characters from each token except parentheses and period
    tokens = [''.join(e for e in token if e in allowed_chars) for token in tokens]
    
    # Remove stop words
    stop_words = set(stopwords.words('english'))
    tokens = [token for token in tokens if token.lower() not in stop_words]
    
    # Remove empty tokens
    tokens = [token for token in tokens if token.strip()]
    
    # Join the cleaned tokens back into a string
    cleaned_text = ' '.join(tokens)
    return cleaned_text

def extract_nutrients(text):
  # Define regular expressions for different nutrients

    extracted_nutrients = {}
    for nutrient, pattern in nutrient_patterns.items():
        match = re.search(pattern, text, re.IGNORECASE)
        if match:
            print("matched ",nutrient)
            value=None 
            unit =None
            flag =0
            print("matched", nutrient , match.groups())
            for i, group in enumerate(match.groups(), start=1):
                print(nutrient , group)
                if group:
                    group = group.strip()
                    if group.replace('.', '', 1).isdigit() and flag==0:
                        value = float(group)
                        print(nutrient , "value = ",value, unit)
                        flag =1
                    elif ( group.lower()=='o'):
                        value =0
                        print(nutrient , "value = ",value, unit)
                    elif group.lower()=='l':
                        value =1
                        print(nutrient , "value = ",value, unit)
                    elif group in ['g', 'mg', 'mcg','mog','µg','ml']:
                        unit = group
                        print(nutrient , "value = ",value, unit)
                    elif group in ['%']:
                        print(nutrient , "value = ",value, unit,end=" ")
                        value=None
                        print(nutrient , "value = ",value, unit)
                        continue
            if (unit is None and value is not None and (int(value)%10==9 or int(value)%10 ==0) and value==int(value)):
                # unit ='g'
                print(nutrient , "value = ",value, unit) 
                value= str(int(value)//10)
            if(unit is not None and value is None):
                value=0
            # if (unit=="mg"):
            #     print(nutrient,"initial value ",value ,end=" ")
            #     value = value/1000
            #     print("new value ",value)
            #     unit ="g"
            # elif unit =="mcg" or unit =="mog" or unit =='µg':
            #     # print(nutrient,"initial value", value,end=" ")
            #     value= value/1000000
            #     # print("new value",value)
            #     unit ="g"
            elif unit is None :
                unit = 'g'
            if value is not None :
                print("before adding the data ",nutrient, value , unit )
                extracted_nutrients[nutrient] = f"{value} {unit}"
    for key , value in extracted_nutrients.items():
        print(key , value)
        
    for incorrect_nutrient,correct_nutrient in nutrient_correction.items():
        if incorrect_nutrient in extracted_nutrients.keys():
            extracted_nutrients[correct_nutrient]=extracted_nutrients.pop(incorrect_nutrient)
    # for incorrect_nutrient, correct_nutrient in nutrient_correction.items():
    #     if incorrect_nutrient in extracted_nutrients:
    #         # If the incorrect nutrient is found, replace it with the correct one
    #         value = extracted_nutrients.get(incorrect_nutrient)
    #         if value is None or value =='0 g' or value =='0.0 g':
    #             extracted_nutrients.pop(incorrect_nutrient)
    #         else:
    #             value = extracted_nutrients.get(correct_nutrient)
    #             if value is not None :
    #                 extracted_nutrients.pop(incorrect_nutrient)
    #             else:
    #                 extracted_nutrients[correct_nutrient] = extracted_nutrients[incorrect_nutrient]
    #                 extracted_nutrients.pop(incorrect_nutrient)
    #             pass
            
            
            
            
            
            
    #         # many times correct and incorrect both may match so remove the incorrect and keep the correct
    #         # one in that case
    #         if value is not None :
    #             extracted_nutrients.pop(incorrect_nutrient)
    #         else:
    #             extracted_nutrients[correct_nutrient] = extracted_nutrients[incorrect_nutrient]
    #             extracted_nutrients.pop(incorrect_nutrient)
    print("after corrections")
    for key , value in extracted_nutrients.items():
        print(key , value)
    for nutrient in nutrients:
        if nutrient not in extracted_nutrients:
            extracted_nutrients[nutrient] = "0.0 g"
    # print("part 2")
    # for key , value in extracted_nutrients.items():
    #     #print(key , value)
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
    output=output.lower()
    return output

# Example usage
# ocr_text = detect_text(r"demo_data\label 9.jpg")
# print("OCR Text Output:\n", ocr_text)  # print the raw OCR text output for inspection

# cleaned_text = clean_ocr_text(ocr_text)
# print("\nCleaned Text:\n", cleaned_text)  # print the cleaned text for inspection
# print(extract_nutrients(cleaned_text))



    