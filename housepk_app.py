# housepk_app.py - Fresh Start
from flask import Flask

app = Flask(__name__)
@app.route('/')
def home():
    return "Home Page for both alice and fatima"

if __name__ == "__main__":
    app.run(debug=True, port=5000)

@app.route('/about')
def about():
    return "About Page for both alice and fatima"

if __name__ == "__main__":
    app.run(debug=True, port=5000)

