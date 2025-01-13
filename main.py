from datetime import datetime
from random import randint
import requests
import json
import pandas as pd
import matplotlib as plt
import numpy as np
from City import City
from utilities import get_weather_forcast
from constants import *

temperature_units = "Fahrenheit"
# Get the weather forcast for the cities
Hayward = City(hayward_latitude, hayward_longitude, "Hayward")
print(Hayward.get_coordinates())

hayward_weather = get_weather_forcast(Hayward.get_latitude(), Hayward.get_longitude())
san_francisco_weather = get_weather_forcast(san_francisco_latitude, san_francisco_longitude)
oakland_weather = get_weather_forcast(oakland_latitude, oakland_longitude)
el_cerrito_weather = get_weather_forcast(el_cerrito_latitude, el_cerrito_longitude)
berkeley_weather = get_weather_forcast(berkeley_latitude, berkeley_longitude)

# Parse the JSON string into a Python dictionary
hayward_data = json.loads(hayward_weather.text)
hayward_temperature_today = hayward_data['properties']['periods'][0]['temperature']
#TODO: Have a Celsisus option

# Format the JSON data with indentation
formatted_json = json.dumps(hayward_data['properties'], indent=4)

# Print the formatted 
print(formatted_json)
print(f"The temperature in Hayward today is {hayward_temperature_today} degrees {temperature_units}")