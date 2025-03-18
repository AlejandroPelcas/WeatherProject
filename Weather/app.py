from flask import Flask, request, render_template, url_for, jsonify, redirect
from main import fetch_weather, fetch_recommendation, fetch_recommendation_data, fetch_info, fetch_lat_lon_weather
from flask_cors import CORS
from flask_wtf import FlaskForm
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user 
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, ValidationError
from flask_bcrypt import Bcrypt #hasing algo for hashing passwords
import sqlite3

DATABASE_NAME = 'User.db'

app = Flask(__name__, static_folder='static') # static_folder helps find the location of static folders such as js
CORS(app)  # This allows all origins
app.secret_key = 'my_secret_key'
bcyrpt = Bcrypt(app) #allows app to use Bcrypt features

#Login Manager releated code
login_manager = LoginManager()
login_manager.init_app(app) # Connects manager with app
login_manager.login_view = "login"
@login_manager.user_loader # reload from user_id store and load

class RegisterForm(FlaskForm):
    username = StringField(validators=[InputRequired(), Length(
        min=4, max=20)], render_kw={"placeholder": "Username"})
    
    password = StringField(validators=[InputRequired(), Length(
    min=4, max=20)], render_kw={"placeholder":"Password"})

    submit = SubmitField("Register")

    # def validate_username(self, username):

    #     existing_user_name = User.query.filter_by(
    #         username=username.data).first()
        

    #     )

class LoginForm(FlaskForm):
    username = StringField(validators=[InputRequired(), Length(
        min=4, max=20)], render_kw={"placeholder": "Username"})
    
    password = StringField(validators=[InputRequired(), Length(
    min=4, max=20)], render_kw={"placeholder":"Password"})

    submit = SubmitField("Login")

@app.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    return render_template('login.html', form=form)


@app.route('/register', methods=['GET','POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        hashed_password = bcyrpt.generate_password_hash(form.password.data)
        # conn = sqlite3.connect(DATABASE_NAME)
        # curs = conn.cursor()
        # curs.execute("")

        # conn.commit()
        # conn.close()
        return redirect(url_for('login'))
    
    return render_template('register.html', form=form)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/info', methods=['GET'])
def info():
    data = fetch_info()

@app.route('/recommendation', methods=['GET'])
def recommendation():
    # Extract the assistant's response
    assistant_message = fetch_recommendation().choices[0].message.content
    # Return the assistant's response as JSON
    return jsonify({"response": assistant_message})


@app.route("/weather/", methods=["GET"])
def weather():
    lat = request.args.get('lat')
    lon = request.args.get('lon')
    if lat and lon:
        data = fetch_lat_lon_weather(lat,lon)
        return data 
    data = fetch_weather()
    return data

@app.route('/recommendation_data/', methods=['GET'])
def recommendation_data():
    temp = request.args.get("temperature")
    humidity = request.args.get("humidity")
    city = request.args.get("city")
    # Extract the assistant's response
    #TODO: Curretnly data is a string object. Need to fix that before passign to fetch_rec
    assistant_message = fetch_recommendation_data(temp,humidity,city).choices[0].message.content
    # Return the assistant's response as JSON
    return jsonify({"response": assistant_message})

# This is just to get the data. Planned to use as part of CSS container to show data in a graph
@app.route('/data', methods=['GET'])
def data():
    data = fetch_weather()
    return data

if __name__ == '__main__':
    app.run(debug=True)