import sqlite3
import requests
import os

from dotenv import load_dotenv
from datetime import datetime


# Loads the variables in .env file
load_dotenv()

# SQLite database configuration
DATABASE_NAME = "weather_data.db"

# OpenWeatherMap API configuration
API_KEY = os.getenv("API_KEY")
CITY = "Berkeley"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

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

def main():
    # Create the database and table if they don't exist
    create_database()

    # Fetch weather data
    weather_data = fetch_weather()
    if weather_data:
        # Store weather data in the database
        store_weather_data(weather_data)
        print("Successfully created and stored weather data")

if __name__ == "__main__":
    main()

