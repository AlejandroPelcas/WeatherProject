import requests
from typing import List
from Weather.City import City

def get_weather_forcast(latitude, longitude):
    """Get the weather forcast of a city for a given latitude and longitude
    Args:
        latitude: float
        longitude: float
        Returns: JSON object of the weather forcast"""
    response = requests.get(f"https://api.weather.gov/points/{latitude},{longitude}")
    forcast_url = response.json()['properties']['forecast']
    return requests.get(forcast_url)


def get_all_forcasts(Cities: List[City]):
    """Get the weather forcast for a list of cities
    Args:
        Cities: List of City objects
        Returns: Dictionary of city and their weather forcasts"""
    forcasts = {}
    for city in Cities:
        forcasts[city.get_name()] = get_weather_forcast(city.get_latitude(), city.get_longitude())
    return forcasts

def load_to_csv(data):  
    """Load the weather forcast data to a CSV file
    Args:
        data: """
    