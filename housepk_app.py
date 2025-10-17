# app.py - Combined Fatima, Alice & Bob's Features
import os
import joblib
import numpy as np
from flask import Flask, render_template, request, jsonify, redirect, url_for

APP_ROOT = os.path.dirname(__file__)
MODEL_DIR = os.path.join(APP_ROOT, "models")

# Load artifacts
model = joblib.load(os.path.join(MODEL_DIR, "house_price_model.pkl"))
feature_list = joblib.load(os.path.join(MODEL_DIR, "model_features.pkl"))
label_encoders = joblib.load(os.path.join(MODEL_DIR, "label_encoders.pkl"))
feature_field_map = joblib.load(os.path.join(MODEL_DIR, "feature_field_map.pkl"))

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

# Combined routes from all three team members
@app.route('/login')
def login():
    return "Login Page - Added by Fatima"

@app.route('/register')
def register():
    return "User Registration - Fatima's Feature"

@app.route('/dashboard')
def dashboard():
    return "Analytics Dashboard - Added by Alice"

@app.route('/stats')
def statistics():
    return "Price Statistics - Alice's Feature"

@app.route('/api/predict')
def api_predict():
    return "API Predict - Added by Bob"

@app.route('/api/docs')
def api_documentation():
    return "API Documentation - Bob's Feature"

@app.route('/')
def home():
    return "Home Page with Authentication, Dashboard and API Features"

@app.route("/predict", methods=["POST"])
def predict():
    # Use the original function name
    return "Prediction page - Final combined version"

if __name__ == "__main__":
    app.run(debug=True, port=5000)  # Use original port