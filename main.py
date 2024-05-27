import os, io,re
from google.cloud import vision,vision_v1
from google.cloud.vision_v1 import types
from importlib.resources import path
import pandas as pd
from dotenv import load_dotenv
load_dotenv()

os.environ["GOOGLE_APPLICATION_CREDENTIALS"]=r'healthkart-catelogging-57eaebe5246c.json'

client = vision.ImageAnnotatorClient()

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
  nutrient_patterns = {
      #"Calories": r"Calories\s*([a-zA-Z]|\d+)",
      "Total Fat": r"Total Fat\s*(\d+)(g|mg|mcg)?",
      "Saturated Fat": r"Saturated Fat\s*([a-zA-Z]|\d+)(g|mg|mcg)?",
      "Trans Fat": r"Trans Fat\s*([a-zA-Z]|\d+)(g|mg|mcg)?",
      "Cholesterol": r"Cholesterol\s*([a-zA-Z]|\d+)(g|mg|mcg)?",
      "Sodium": r"Sodium\s*([a-zA-Z]|\d+)(g|mg|mcg)?",
      "Dietary Fiber": r"Dietary Fiber\s*([a-zA-Z]|\d+)(g|mg|mcg)?",
      "Total Carbohydrate": r"(Total\s)?Carbohydrates?\s*([a-zA-Z]|\d+)(g|mg|mcg)?",
      "Total Sugars": r"Total Sugars\s*([a-zA-Z]|\d+)(g|mg|mcg)?",
    #   "Added Sugars": r"Incl\.\s*(\d+)(?:g) Added Sugars",
      "Protein": r"Protein\s*([a-zA-Z]|\d+)(g|mg|mcg)?",
    #   "Potassium": r"Potassium\s*([a-zA-Z]|\d+)(g|mg|mcg)?",
      "Potassium": r"Potassium\s*([\d.]+)\s*(mg|g|mcg)?",
      "Vitamin A": r"Vitamin A\s*([\d.]+)\s*(mg|g|mcg)?",
      "Vitamin B6": r"Vitamin B6\s*([\d.]+)\s*(mg|g|mcg)?",
      "Vitamin B12": r"Vitamin B12\s*([\d.]+)\s*(mg|g|mcg)?",
      "Vitamin C": r"Vitamin C\s*([\d.]+)\s*(mg|g|mcg)?",
      "Vitamin D": r"Vitamin D\s*([\d.]+)\s*(mg|g|mcg)?",
      "Vitamin E": r"Vitamin E\s*([\d.]+)\s*(mg|g|mcg)?",
      "Vitamin K": r"Vitamin K\s*([\d.]+)\s*(mg|g|mcg)?",
      "Calcium": r"Calcium\s*([a-zA-Z]|\d+)(g|mg|mcg)?",
      "Iron": r"Iron\s*([a-zA-Z]|\d+(\.\d+)?)(g|mg|mcg)?"
  }
  
  extracted_nutrients = {}
  for nutrient, pattern in nutrient_patterns.items():
      match = re.search(pattern, text, re.IGNORECASE)
      if match:
          value=None 
          unit =None
          for i, group in enumerate(match.groups(), start=1):
            # if group and group.isdigit():
            #     value =group
            if group and group.replace('.', '', 1).isdigit():
                value = float(group)
            elif ( group and group.lower()=='o'):
                value =0
            elif group and group.lower()=='l':
                value =1
            elif group and group in ['g', 'mg', 'mcg']:
                unit = group
            elif (unit is None and value is not None):
                unit ='g'
                if (int(value)%10==9 or int(value)%10 ==0):
                    value = int(value)//10
          if value is not None :
              extracted_nutrients[nutrient] = f"{value} {unit}"
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
# # print("OCR Text Output:\n", ocr_text)  # Print the raw OCR text output for inspection

# cleaned_text = clean_ocr_text(ocr_text)
# print("\nCleaned Text:\n", cleaned_text)  # Print the cleaned text for inspection
# print(extract_nutrients(cleaned_text))



    