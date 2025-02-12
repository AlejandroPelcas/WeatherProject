from flask import Flask, render_template
from main import fetch_weather
from flask_cors import CORS

app = Flask(__name__, static_folder='/Users/alejandropelcastre/Alejandros_projects/WeatherProject/WeatherProject/Weather2/js')
CORS(app)  # This allows all origins

@app.route('/')
def home():
    return render_template("index.html")

@app.route("/weather", methods=["GET"])
def weather():
    data = fetch_weather()
    print('GOT THE WEATHER DATA', data)
    return data

print("Still working")
data = weather()


if __name__ == '__main__':
    app.run(debug=True)