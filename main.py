import os, io,re
from google.cloud import vision,vision_v1
from google.cloud.vision_v1 import types
from importlib.resources import path
import pandas as pd
import google.generativeai as genai 
from dotenv import load_dotenv
load_dotenv()

# load gemini model
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel("gemini-pro")
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
  """
  Extracts nutrients and their values from a text block containing nutritional information.

  Args:
      text: The text containing the nutritional information.

  Returns:
      A dictionary mapping nutrient names to their corresponding values.
  """
  # Define regular expressions for different nutrients
  nutrient_patterns = {
      #"Calories": r"Calories\s*([a-zA-Z]|\d+)",
      "Total Fat": r"Total Fat\s*([a-zA-Z]|\d+)(g|mg|mcg)?",
      "Saturated Fat": r"Saturated Fat\s*([a-zA-Z]|\d+)(g|mg|mcg)?",
      "Trans Fat": r"Trans Fat\s*([a-zA-Z]|\d+)(g|mg|mcg)?",
      "Cholesterol": r"Cholesterol\s*([a-zA-Z]|\d+)(g|mg|mcg)?",
      "Sodium": r"Sodium\s*([a-zA-Z]|\d+)(g|mg|mcg)?",
      "Dietary Fiber": r"Dietary Fiber\s*([a-zA-Z]|\d+)(g|mg|mcg)?",
      "Total Carbohydrate": r"Total Carbohydrate\s*([a-zA-Z]|\d+)(g|mg|mcg)?",
      "Total Sugars": r"Total Sugars\s*([a-zA-Z]|\d+)(g|mg|mcg)?",
    #   "Added Sugars": r"Incl\.\s*(\d+)(?:g) Added Sugars",
      "Protein": r"Protein\s*([a-zA-Z]|\d+)(g|mg|mcg)?",
      "Potassium": r"Potassium\s*([a-zA-Z]|\d+)(g|mg|mcg)?",
      "Vitamin A": r"Vitamin A\s*([a-zA-Z]|\d+)(g|mg|mcg)?",
      "Calcium": r"Calcium\s*([a-zA-Z]|\d+)(g|mg|mcg)?",
      "Iron": r"Iron\s*([a-zA-Z]|\d+)(g|mg|mcg)?"
  }
  
#   extracted_nutrients = {}
#   for nutrient, pattern in nutrient_patterns.items():
#     match = re.search(pattern, text)
#     if match:
#         extracted_nutrients[nutrient] = match.group(1)+match.group(2)
#   return extracted_nutrients
  extracted_nutrients = {}
  for nutrient, pattern in nutrient_patterns.items():
      match = re.search(pattern, text, re.IGNORECASE)
      if match:
          value = match.group(1)
          unit = match.group(2) if match.group(2) else "g"  # Default unit to grams if not specified
          extracted_nutrients[nutrient] = f"{value} {unit}"
  return extracted_nutrients



# def parse_nutrient_info_with_regex(cleaned_text):
#     # Adjust the regex pattern to match the cleaned text structure
#     pattern = r'([A-Za-z\s]+)\s*[:|]\s*([\d.]+\s*(?:mg|g|mcg|kcal|%|calories|cal|cup|servings|container|oz))'
#     matches = re.findall(pattern, cleaned_text, re.IGNORECASE)
    
#     # If the pattern does not match, try a different approach
#     if not matches:
#         pattern = r'([A-Za-z\s]+)\s*([\d.]+\s*(?:mg|g|mcg|kcal|%|calories|cal|cup|servings|container|oz))'
#         matches = re.findall(pattern, cleaned_text, re.IGNORECASE)
    
#     nutrients = {match[0].strip(): match[1].strip() for match in matches}
#     return nutrients

def create_dataframe(nutrients_dict):
    df = pd.DataFrame(list(nutrients_dict.items()), columns=['Nutrient', 'Quantity'])
    return df



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

def generate_gemini_content(ocr_text):
    model = genai.GenerativeModel("gemini-pro")
    prompt =f'''You need to extraction all the nutrients present in the text and create a table containing the nutrient and its quantity the text is here : {ocr_text}'''
    response = model.generate_content(prompt)

# Example usage
ocr_text = detect_text(r"data\label3.jpg")
# print("OCR Text Output:\n", ocr_text)  # Print the raw OCR text output for inspection

cleaned_text = clean_ocr_text(ocr_text)
# print("\nCleaned Text:\n", cleaned_text)  # Print the cleaned text for inspection
print(extract_nutrients(cleaned_text))



    