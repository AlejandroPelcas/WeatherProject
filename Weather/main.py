import sqlite3
import requests
import os
from dotenv import load_dotenv
from datetime import datetime
from openai import OpenAI

# Loads the variables in .env file
load_dotenv()

# Connect to OpenAI api
client = OpenAI()
OpenAI.api_key = os.getenv("OPENAI_API_KEY")

# SQLite database configuration
DATABASE_NAME = "weather_data.db"

# OpenWeatherMap API configuration
API_KEY = os.getenv("API_KEY")
CITY = "Berkeley"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def fetch_recommendation_data(temp, humidity, city):
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {
                "role": "user",
                "content": f"""The current temperatures and humidity are {temp} degrees and {humidity}%s.
                I currently live in {city}. What's the most appropriate thing to wear? 
                Respond in the following way: The current temperatue is {temp} with humidity percentage {humidity}.
                You are also in {city}. The best clothes to wear are: And list the clothes"""
            }
        ]
    )
     #type of data is that of chatCompletion
    return completion

def fetch_recommendation():
    # if data == None:
    #     print("Data field empty")
    #     completion = client.chat.completions.create(
    #     model="gpt-4o-mini",
    #     messages=[
    #         {"role": "system", "content": "You are a helpful assistant."},
    #         {
    #             "role": "user",
    #             "content": "What is ${temp} celsius in farenheit?. What should I wear?"
    #         }
    #     ]
    #     )
    #     #type of data is that of chatCompletion
    #     return completion
    
    #If data was passed in use it 
    print("Data was passed in fetch rec")
    # temp = data['temperature']
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {
                "role": "user",
                "content": "What is  celsius in farenheit?. What should I wear?"
            }
        ]
    )
     #type of data is that of chatCompletion
    return completion

def create_database():
    """ Creates SQLite database to store weather data """
    connection = sqlite3.connect(DATABASE_NAME)
    cursor = connection.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS weather (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            city TEXT,
            temperature REAL,
            humidity INTEGER,
            weather_description TEXT,
            timestamp DATETIME
        )
    ''')
    connection.commit()
    connection.close()

def fetch_weather_data():
    """ Fetch the current weather data from OpenWeatherApi"""
    params =  {
        "q": CITY,
        "appid": API_KEY,
        "units": "metric"  # Use "imperial" for Fahrenheit
    }
    response = requests.get(BASE_URL, params=params) # Gives back a resposne Object: Need to turn to json
    if response.status_code == 200:
        print("API Response Successful")
        data = response.json()
        return {
            "city": data["name"],
            "temperature": data["main"]["temp"],
            "humidity": data["main"]["humidity"],
            "weather_description": data["weather"][0]["description"],
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
    else:
        print(f"Error fetching weather data: {response.status_code}")
        return None
    
def fetch_info():
    params =  {
        "q": CITY,
        "appid": API_KEY,
        "units": "metric"  # Use "imperial" for Fahrenheit
    }
    response = requests.get(BASE_URL, params=params) # Gives back a resposne Object: Need to turn to json
    if response.status_code == 200:
        print("API Response Successful")
        data = response.json()
        return data
    else:
        print(f"Error fetching weather data: {response.status_code}")
        return None
    
def fetch_lat_lon_weather(lat, lon):
    url= BASE_URL + f"/?lat={lat}&lon={lon}&appid={API_KEY}"
    params =  {
        "appid": API_KEY,
        "units": "metric"  # Use "metric" for Celsius
    }
    response = requests.get(url, params=params) # Gives back a resposne Object: Need to turn to json
    if response.status_code == 200:
        data = response.json()
        return {
            "city": data["name"],
            "temperature": data["main"]["temp"],
            "humidity": data["main"]["humidity"],
            "weather_description": data["weather"][0]["description"],
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
    else:
        print(f"MAIN.PY Error fetching weather data: {response.status_code}")
        return None
#TODO: Rename this to 'fetch_weather_data' and change other method's name
def fetch_weather():
    params =  {
        "q": CITY,
        "appid": API_KEY,
        "units": "metric"  # Use "metric" for Celsius
    }
    response = requests.get(BASE_URL, params=params) # Gives back a resposne Object: Need to turn to json
    if response.status_code == 200:
        data = response.json()
        return {
            "city": data["name"],
            "temperature": data["main"]["temp"],
            "humidity": data["main"]["humidity"],
            "weather_description": data["weather"][0]["description"],
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
    else:
        print(f"MAIN.PY Error fetching weather data: {response.status_code}")
        return None
    

def store_weather_data(weather_data):
    """Store weather data in the SQLite database."""
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO weather (city, temperature, humidity, weather_description, timestamp)
        VALUES (?, ?, ?, ?, ?)
    ''', (
        weather_data["city"],
        weather_data["temperature"],
        weather_data["humidity"],
        weather_data["weather_description"],
        weather_data["timestamp"]
    ))
    conn.commit()
    conn.close()
    print("Weather data stored successfully!")

def create_user_database():
    conn = sqlite3.connect('User.db')
    cur  = conn.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS Users (
                id INTEGER NOT NULL,
                username varchar(20) NOT NULL UNIQUE,
                password varchar(20) NOT NULL
                )""")
    print("Successfully created user-base db")
    conn.commit()
    conn.close()

def main():
    # Create the database and table if they don't exist
    create_database()
    create_user_database()
    # Fetch weather data
    weather_data = fetch_weather()
    if weather_data:
        # Store weather data in the database
        store_weather_data(weather_data)
        print("Successfully created and stored weather data")

if __name__ == "__main__":
    main()