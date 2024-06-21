from flask import Flask, jsonify, request
from flask_cors import CORS
import werkzeug
import werkzeug.utils
from main import *
import os 

app = Flask(__name__)
CORS(app)
port =8000

# Create upload folder if it doesn't exist
UPLOAD_FOLDER = './uploaded_images/'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)


@app.route('/api/message', methods=['GET'])
def get_message():
    return jsonify({"message": "Backend will be built soon"})

@app.route('/api/upload_image',methods=['POST'])
def get_image_content():
    if (request.method=="POST"):
        imagefile = request.files['image']
        filename = werkzeug.utils.secure_filename(imagefile.filename)
        filepath = os.path.join(UPLOAD_FOLDER, filename)
        imagefile.save(filepath)
        detected_text = detect_text(filepath)
        cleaned_text = clean_ocr_text(detected_text)
        output = extract_nutrients(detected_text)
        df = pd.DataFrame(list(output.items()), columns=['Nutrient', 'Value'])
        if(cleaned_text !=""):
            return jsonify({
                "message":cleaned_text,
                "nutrients":df.to_dict(orient='records'),
            })
        else :
            return jsonify({
                "message":"Could not extract any text",
                "nutrients":None,
            })

if __name__ == '__main__':
    print(f"Server is listening to http://127.0.0.1:{port}")
    app.run(debug=True, port=port)
