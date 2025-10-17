# app.py - Alice's Version
import os
import joblib
import numpy as np
from flask import Flask, render_template, request, jsonify

APP_ROOT = os.path.dirname(__file__)
MODEL_DIR = os.path.join(APP_ROOT, "models")

# Load artifacts
model = joblib.load(os.path.join(MODEL_DIR, "house_price_model.pkl"))
feature_list = joblib.load(os.path.join(MODEL_DIR, "model_features.pkl"))
label_encoders = joblib.load(os.path.join(MODEL_DIR, "label_encoders.pkl"))
feature_field_map = joblib.load(os.path.join(MODEL_DIR, "feature_field_map.pkl"))

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

# Alice's dashboard routes
@app.route('/dashboard')
def dashboard():
    return "Analytics Dashboard - Added by Alice"

@app.route('/stats')
def statistics():
    return "Price Statistics - Alice's Feature"

@app.route('/')
def index():
    return "Home Page with Dashboard - Alice's Version"

@app.route("/predict", methods=["POST"])
def predict_price():
    # Alice renamed the function
    return "Prediction page - Alice's version"

if __name__ == "__main__":
    app.run(debug=True, port=5001)  # Alice changed port