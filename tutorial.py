import requests
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
