# housepk_app.py - Alice's Version  
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return \"📊 Home with Dashboard - Alice\"

@app.route('/dashboard')
def dashboard():
    return \"📈 Dashboard - Alice\"

if __name__ == \"__main__\":
    app.run(debug=True, port=5001)
