from PIL import Image
import os
import tempfile
from main import *
from mongo import *

labels =os.listdir('data')
print(labels)
for label in labels :
    label_images_path= os.listdir(os.path.join('data',label))
    for label_image_path in label_images_path:
        try:
            detected_text = detect_text(os.path.join('data',label,label_image_path))
            cleaned_text = clean_ocr_text(detected_text)
            output = extract_nutrients(cleaned_text)
            output["label"]=label
            output["image_path"]=os.path.join('data',label,label_image_path)
            # print(output)
            if (set(output.keys())=={"label","image_path"}):
                print("Skipping image as this is very blurry")
            else:
                insert_to_db(output, "HealthKart" , "Food Catelogs")
        except Exception as e:
            print(f"An Error occured {e}")