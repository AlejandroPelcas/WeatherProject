import requests

def get_weather_forcast(latitude, longitude):
    """Get the weather forcast of a city for a given latitude and longitude"""
    response = requests.get(f"https://api.weather.gov/points/{latitude},{longitude}")
    forcast_url = response.json()['properties']['forecast']
    return requests.get(forcast_url)