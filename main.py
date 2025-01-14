from datetime import datetime
from random import randint
import requests
import json
import numpy as np
from City import City
from utilities import *
from constants import *
from pyspark.sql import SparkSession

TEMPERATURE_UNITS = "Fahrenheit"

# Spark session
# spark = SparkSession.builder.appName("WeatherForcast").getOrCreate()

# Get the weather forcast for the cities
weather_forcasts = get_all_forcasts(CITIES)

# Parse the JSON string into a Python dictionary

# TODO: Here probably write to a database/file
# for city in CITIES.keys():

hayward_data = json.loads(weather_forcasts["Hayward"].text)

# Data to collect:
hayward_temperature_today = hayward_data['properties']['periods'][0]['temperature']
hayward_start_time = hayward_data['properties']['periods'][0]['startTime']
hayward_detailed_forecast = hayward_data['properties']['periods'][0]['detailedForecast']
#TODO: Have a Celsisus option

# Format the JSON data with indentation
formatted_json = json.dumps(hayward_data['properties'], indent=4)

# Print the formatted 
print(formatted_json)
print(f"The temperature in Hayward today is {hayward_temperature_today} degrees {TEMPERATURE_UNITS}")
print(f"The detailed forcast for Hayward today is: {hayward_detailed_forecast}, the time is {hayward_start_time}")

if __name__ == '__main__':
    pass