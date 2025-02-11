from flask import Flask
from main import fetch_weather

app = Flask(__name__)

@app.route('/')
def home():
    return "<p> You made it to homepage </p>"

@app.route("/weather ", methods=["GET"])
def weather():
    data = fetch_weather()
    return data

print("Still working")
data = weather()


if __name__ == '__main__':
    app.run(debug=True)