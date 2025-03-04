from flask import Flask, render_template, jsonify
from main import fetch_weather, fetch_recommendation
from flask_cors import CORS
# static_folder helps find the location of static folders such as js
app = Flask(__name__, static_folder='static')
CORS(app)  # This allows all origins

@app.route('/')
def home():
    return render_template("index.html")

@app.route("/weather", methods=["GET"])
def weather():
    data = fetch_weather()
    print('GOT THE WEATHER DATA', data)
    return data

@app.route('/recommendation', methods=['GET'])
def recommendation():
    # Extract the assistant's response
    assistant_message = fetch_recommendation().choices[0].message.content
    # Return the assistant's response as JSON
    return jsonify({"response": assistant_message})

# This is just to get the data. Planned to use as part of CSS container to show data in a graph
@app.route('/data', methods=['GET'])
def data():
    data = fetch_weather()
    return data

if __name__ == '__main__':
    app.run(debug=True)