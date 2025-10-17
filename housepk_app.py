# housepk_app.py - Fatima's Version
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return \"🔐 Home with Login - Fatima\"

@app.route('/login')
def login():
    return \"🔑 Login Page - Fatima\"

if __name__ == \"__main__\":
    app.run(debug=True, port=5000)
