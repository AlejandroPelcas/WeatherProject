from City import City
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

CITIES = [
    City(hayward_latitude, hayward_longitude, "Hayward"),
    City(el_cerrito_latitude, el_cerrito_longitude, "El Cerrito"),
    City(san_francisco_latitude, san_francisco_longitude, "San Francisco"),
    City(oakland_latitude, oakland_longitude, "Oakland"),
    City(berkeley_latitude, berkeley_longitude, "Berkeley")
]