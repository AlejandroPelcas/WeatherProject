from datetime import datetime
from random import randint
import requests
import json
import pandas as pd
import matplotlib as plt
import numpy as np
from utilities import get_weather_forcast
import constants

# Get the weather forcast:
# First you need to use the latitude and longitude of the location you want to get the weather forcast for.
# Next you need to use the response from the request to find the forecast url.
# Finally you can use the forecast url to get the weather forcast.`
longitude = -122.4194
latitude = 37.7749
response = requests.get(f"https://api.weather.gov/points/{latitude},{longitude}")

# Get the forecast url from the response 
forcast_url = response.json()['properties']['forecast']

response = requests.get(forcast_url)
print(response.json())


# Get the weather forcast for the cities
hayward_weather = get_weather_forcast(constants.hayward_latitude, constants.hayward_longitude)
san_francisco_weather = get_weather_forcast(constants.san_francisco_latitude, constants.san_francisco_longitude)
oakland_weather = get_weather_forcast(constants.oakland_latitude, constants.oakland_longitude)
el_cerrito_weather = get_weather_forcast(constants.el_cerrito_latitude, constants.el_cerrito_longitude)
berkeley_weather = get_weather_forcast(constants.berkeley_latitude, constants.berkeley_longitude)

# Print the weather forcast for the cities
print(hayward_weather.json())

# Parse the JSON string into a Python dictionary
data = json.loads(hayward_weather.text)

# Format the JSON data with indentation
formatted_json = json.dumps(data, indent=4)

# Print the formatted 
print(formatted_json)
