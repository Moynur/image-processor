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

def extract_items(text, items_dict):
    lines = text.split("\n")
    extracted_items = []
    for line in lines:
        for item in items_dict:
            if item.lower() in line.lower():
                extracted_items.append(item)
                break
    return extracted_items


grocery_dict = {
    "apple": "apple - 1 kg",
    "banana": "banana - 500 g",
    "broccoli": "broccoli - 200 g",
    "carrot": "carrot - 1 kg",
    "celery": "celery - 500 g",
    "spaghetti": "bla"
}

@app.route("/", methods=["POST"])
def process_image():
    print("got a request")
    image = request.files.get("image")
    image_data = image.read()
    image_data = base64.b64encode(image_data).decode("utf-8")
    text = extract_text(image_data)
    print("hello", text)
    items = extract_items(text, grocery_dict)
    return jsonify({"items": items})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
