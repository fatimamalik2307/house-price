# housepk_app.py - Fresh Start for Git Exercise
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return \"🏠 Home Page - Clean Start\"

@app.route('/about')
def about():
    return \"📖 About Page\"

if __name__ == \"__main__\":
    app.run(debug=True, port=5000)
