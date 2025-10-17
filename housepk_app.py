# housepk_app.py - Fresh Start
from flask import Flask

app = Flask(__name__)
@app.route('/')
def home():
    return "🚨 Alice's Home Page - CONFLICT VERSION"

@app.route('/about')
def about():
    return "About Page for alice"

if __name__ == "__main__":
    app.run(debug=True, port=5000)
