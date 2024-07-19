## HealthKart Food Label Cataloging Application
### Overview
This application is designed to process images of food labels, extract nutritional information, and determine whether the food is healthy or unhealthy. It leverages Google Cloud Vision for OCR (Optical Character Recognition) and a generative AI model to analyze the text. The processed data is then stored in a MongoDB database.
### Features
- Upload an image or provide a URL to an image for processing.
- Perform OCR to detect and clean text from the image.
- Extract nutritional information from the detected text.
- Adjust nutrient values based on the serving size.
- Determine if the food is healthy or unhealthy using a generative AI model.
- Store the processed data in a MongoDB database.
### Prerequisites
- Python 3.10 or higher
- Google Cloud Vision API credentials
- Google Generative AI API key
- MongoDB for data storage
### Installation
1. Clone the repository:
    ```
    git https://github.com/Adi123XD/Food-Cateloging-.git
    cd Food-Cateloging-
   ```
