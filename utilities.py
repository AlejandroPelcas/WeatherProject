import requests

def get_weather_forcast(latitude, longitude):
    """Get the weather forcast of a city for a given latitude and longitude"""
    response = requests.get(f"https://api.weather.gov/points/{latitude},{longitude}")
    forcast_url = response.json()['properties']['forecast']
    return requests.get(forcast_url)

def get_all_forcasts(cities):
    """Get the weather forcast for a list of cities"""
    forcasts = {}
    for city, coordinates in cities.items():
        forcasts[city] = get_weather_forcast(coordinates[0], coordinates[1])
    return forcasts