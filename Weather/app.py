from flask import Flask, render_template, jsonify
from main import fetch_weather, fetch_recommendation
from flask_cors import CORS
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, ValidationError

# static_folder helps find the location of static folders such as js
app = Flask(__name__, static_folder='static')
CORS(app)  # This allows all origins

app.secret_key = 'my_secret_key'


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
    return render_template('register.html', form=form)



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

@app.route('/recommendation/<data>', methods=['GET'])
def recommendation_data(data):
    # Extract the assistant's response
    #TODO: Curretnly data is a string object. Need to fix that before passign to fetch_rec
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