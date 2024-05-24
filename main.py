import os, io
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
    return response.text
ocr_text = detect_text(r"data/label5.jpg")
print (ocr_text)
print(generate_gemini_content(ocr_text))
    