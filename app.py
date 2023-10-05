from flask import Flask, render_template, request, jsonify
import tensorflow as tf
from tensorflow import keras
from PIL import Image
import numpy as np

app = Flask(__name__)

# Load the trained model
model = keras.models.load_model("model.h5")

# Define classes
classes = ["glioma", "meningioma", "pituitary", "notumor"]


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/upload", methods=["POST"])
def upload():
    if "image" not in request.files:
        return jsonify({"error": "No file part"})

    image_file = request.files["image"]

    if image_file.filename == "":
        return jsonify({"error": "No selected file"})

    if image_file:
        image = Image.open(image_file)
        image = image.resize((150, 150))  # Resize the image to 150x150
        image = np.array(image)
        image = image / 255.0  # Normalize the image
        image = np.expand_dims(image, axis=0)  # Add batch dimension
        prediction = model.predict(image)
        predicted_class = classes[np.argmax(prediction)]

        return jsonify({"prediction": predicted_class})
