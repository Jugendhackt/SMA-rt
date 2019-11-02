import requests
import json
import math

range = 2 # km
lat = 48.4
lon = 9.98
lat0 = lat + range * (1 / 119.574)
lon0 = lon + range * (1 / (111.320 * math.cos(lat)))
lat1 = lat - range * (1 / 119.574)
lon1 = lon - range * (1 / (111.320 * math.cos(lat)))

overpass_url = "https://overpass-api.de/api/interpreter"
overpass_query = f'''
[out:json][timeout:25];
(
  relation["type"="route"]({lat0},{lon0},{lat1},{lon1});
);
out body;
'''

print(overpass_query)


response = requests.post(overpass_url, {'data': overpass_query})

print(response.text)
#data = response.json()
print(response.json())