from datetime import datetime
from random import randint
import requests
import json
import pandas as pd
import matplotlib as plt
import numpy as np
from City import City
from utilities import *
from constants import *

TEMPERATURE_UNITS = "Fahrenheit"

# Define cities to get the weather forcast
Hayward = City(hayward_latitude, hayward_longitude, "Hayward")
ElCerrito = City(el_cerrito_latitude, el_cerrito_longitude, "El Cerrito")
SanFrancisco = City(san_francisco_latitude, san_francisco_longitude, "San Francisco")
Oakland = City(oakland_latitude, oakland_longitude, "Oakland")
Berkeley = City(berkeley_latitude, berkeley_longitude, "Berkeley")

# Get the weather forcast for the cities
weather_forcasts = get_all_forcasts([Hayward, ElCerrito, SanFrancisco, Oakland, Berkeley])

# Parse the JSON string into a Python dictionary
print(weather_forcasts)
hayward_data = json.loads(weather_forcasts[Hayward].text)
hayward_temperature_today = hayward_data['properties']['periods'][0]['temperature']
#TODO: Have a Celsisus option

# Format the JSON data with indentation
formatted_json = json.dumps(hayward_data['properties'], indent=4)

# Print the formatted 
print(formatted_json)
print(f"The temperature in Hayward today is {hayward_temperature_today} degrees {TEMPERATURE_UNITS}")