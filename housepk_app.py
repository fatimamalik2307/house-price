# app.py - Bob's Version
import os
import joblib
import numpy as np
from flask import Flask, render_template, request

APP_ROOT = os.path.dirname(__file__)
MODEL_DIR = os.path.join(APP_ROOT, "models")

# Load artifacts
model = joblib.load(os.path.join(MODEL_DIR, "house_price_model.pkl"))
feature_list = joblib.load(os.path.join(MODEL_DIR, "model_features.pkl"))
label_encoders = joblib.load(os.path.join(MODEL_DIR, "label_encoders.pkl"))
feature_field_map = joblib.load(os.path.join(MODEL_DIR, "feature_field_map.pkl"))

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

# Bob's API routes
@app.route('/api/predict')
def api_predict():
    return "API Predict - Added by Bob"

@app.route('/api/docs')
def api_documentation():
    return "API Documentation - Bob's Feature"

@app.route('/')
def main():
    return "Home Page with API - Bob's Version"

@app.route("/predict", methods=["POST"])
def make_prediction():
    # Bob renamed the function
    return "Prediction page - Bob's version"

if __name__ == "__main__":
    app.run(debug=True, port=5002)  # Bob changed port