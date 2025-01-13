from datetime import datetime
from random import randint
import requests
import json
import pandas as pd
import matplotlib as plt
import numpy as np

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

# List of cities and their latitude and longitude coordinates 
hayward_latitude = 37.668821
hayward_longitude = -122.080796

san_francisco_latitude = 37.7749
san_francisco_longitude = -122.4194

oakland_latitude = 37.8044
oakland_longitude = -122.2711

el_cerrito_latitude = 37.9150
el_cerrito_longitude = -122.3108

berkeley_latitude = 37.8715
berkeley_longitude = -122.2730

# Get the weather forcast for the cities

def get_weather_forcast(latitude, longitude):
    """Get the weather forcast of a city for a given latitude and longitude"""
    response = requests.get(f"https://api.weather.gov/points/{latitude},{longitude}")
    forcast_url = response.json()['properties']['forecast']
    return requests.get(forcast_url)


hayward_weather = get_weather_forcast(hayward_latitude, hayward_longitude)
san_francisco_weather = get_weather_forcast(san_francisco_latitude, san_francisco_longitude)
oakland_weather = get_weather_forcast(oakland_latitude, oakland_longitude)
el_cerrito_weather = get_weather_forcast(el_cerrito_latitude, el_cerrito_longitude)
berkeley_weather = get_weather_forcast(berkeley_latitude, berkeley_longitude)

# Print the weather forcast for the cities
print(hayward_weather.json())
print(san_francisco_weather.json())
print(oakland_weather.json())