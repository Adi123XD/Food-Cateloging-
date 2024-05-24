import os, io
from google.cloud import vision,vision_v1
from google.cloud.vision_v1 import types
from importlib.resources import path
import pandas as pd

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
# print(detect_text("demo.jpg"))
    