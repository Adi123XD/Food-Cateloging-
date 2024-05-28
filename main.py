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
      "Total Fat": r"Total Fat\s*(\d+(\.\d+)?)(g|mg|mcg|mog)?",
      "Saturated Fat": r"Saturated Fat\s*([a-zA-Z]|\d+(\.\d+)?)(g|mg|mcg|mog)?",
      "Trans Fat": r"Trans Fat\s*([a-zA-Z]|\d+(\.\d+)?)(g|mg|mcg|mog)?",
      "Cholesterol": r"Cholesterol\s*([a-zA-Z]|\d+(\.\d+)?)(g|mg|mcg|mog)?",
      "Sodium": r"Sodium\s*([a-zA-Z]|\d+(\.\d+)?)(g|mg|mcg|mog)?",
      "Dietary Fiber": r"Dietary Fiber\s*([a-zA-Z]|\d+(\.\d+)?)(g|mg|mcg|mog)?",
      "Total Carbohydrate": r"(Total\s)?Carbohydrates?\s*([a-zA-Z]|\d+(\.\d+)?)(g|mg|mcg|mog)?",
      "Total Sugars": r"Total Sugars\s*([a-zA-Z]|\d+(\.\d+)?)(g|mg|mcg|mog)?",
      "Protein": r"Protein\s*([a-zA-Z]|\d+(\.\d+)?)(g|mg|mcg|mog)?",
      "Potassium": r"Potassium\s*([a-zA-Z]|\d+(\.\d+)?)(g|mg|mcg|mog)?",
      "Vitamin A": r"Vitamin A\s*([a-zA-Z]|\d+(\.\d+)?)(g|mg|mcg|mog)?",
      "Vitamin B6": r"Vitamin B6\s*([a-zA-Z]|\d+(\.\d+)?)(g|mg|mcg|mog)?",
      "Vitamin B12": r"Vitamin B12\s*([a-zA-Z]|\d+(\.\d+)?)(g|mg|mcg|mog)?",
      "Vitamin C": r"Vitamin C\s*([a-zA-Z]|\d+(\.\d+)?)(g|mg|mcg|mog)?",
      "Vitamin D": r"Vitamin D\s*([a-zA-Z]|\d+(\.\d+)?)(g|mg|mcg|mog)?",
      "Vitamin E": r"Vitamin E\s*([a-zA-Z]|\d+(\.\d+)?)(g|mg|mcg|mog)?",
      "Vitamin K": r"Vitamin K\s*([a-zA-Z]|\d+(\.\d+)?)(g|mg|mcg|mog)?",
      "Calcium": r"Calcium\s*([a-zA-Z]|\d+(\.\d+)?)(g|mg|mcg|mog)?",
      "Iron": r"Iron\s*([a-zA-Z]|\d+(\.\d+)?)(g|mg|mcg|mog)?"
  }
  
  extracted_nutrients = {}
  for nutrient, pattern in nutrient_patterns.items():
      match = re.search(pattern, text, re.IGNORECASE)
      if match:
        #   print("matched ",nutrient)
          value=None 
          unit =None
          flag =0
          for i, group in enumerate(match.groups(), start=1):
            if group:
                if group.replace('.', '', 1).isdigit() and flag==0:
                    value = float(group)
                    # print(nutrient , value, unit)
                    flag =1
                elif ( group.lower()=='o'):
                    value =0
                    # print(nutrient , value , unit)
                elif group.lower()=='l':
                    value =1
                    # print(nutrient , value , unit)
                elif group in ['g', 'mg', 'mcg','mog']:
                    unit = group
                    # print(nutrient , value , unit)
          if (unit is None and value is not None and (int(value)%10==9 or int(value)%10 ==0)):
            unit ='g'
            # print(nutrient , value , unit , end=" ")
            value= str(int(value)//10)
          if (unit=="mg"):
              # print(nutrient,"initial value ",value ,end=" ")
              value = value/1000
              # print("new value ",value)
              unit ="g"
          elif unit =="mcg" or unit =="mog":
            #   print(nutrient,"initial value", value,end=" ")
              value= value/1000000
            #   print("new value",value)
              unit ="g"
          elif unit is None :
            unit = 'g'
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



    