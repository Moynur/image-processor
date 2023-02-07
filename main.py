# app.py
import base64
import re
import pytesseract
from io import BytesIO
from PIL import Image
from flask import Flask, request, jsonify

app = Flask(__name__)

def extract_text(image_data):
    image = Image.open(BytesIO(base64.b64decode(image_data)))
    return pytesseract.image_to_string(image)

def extract_items(text):
    items = re.findall(r'\d+\s[A-Za-z]+', text)
    return items

@app.route("/", methods=["POST"])
def process_image():
    image = request.files.get("image")
    image_data = image.read()
    image_data = base64.b64encode(image_data).decode("utf-8")
    text = extract_text(image_data)
    items = extract_items(text)
    return jsonify({"items": items})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
