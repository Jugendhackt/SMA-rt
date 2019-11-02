import requests
import json
from math import radians, cos, sin, asin, sqrt

def haversine(lon0, lat0, lon1, lat1):
    lon0, lat0, lon1, lat1 = map(radians, [lon0, lat0, lon1, lat1])
    dlon = lon1 - lon0 
    dlat = lat1 - lat0 
    a = sin(dlat/2)**2 + cos(lat0) * cos(lat1) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a)) 
    r = 6371
    return c * r

range = 2 # km
lat = 48.4
lon = 9.98
lat1 = lat + range * (1 / 110.574)
lon1 = lon + range * (1 / (111.320 * cos(lat)))
lat0 = lat - range * (1 / 110.574)
lon0 = lon - range * (1 / (111.320 * cos(lat)))

overpass_url = "https://lz4.overpass-api.de/api/interpreter"
overpass_query = f'''
[out:json][timeout:25];
(
  node["shop"="bakery"]({lat0},{lon0},{lat1},{lon1});
);
out body;
'''

print(overpass_query)


response = requests.post(overpass_url, {'data': overpass_query})
results = response.json()["elements"]

for result in results:
    if isinstance(result["lon"], float) and isinstance(result["lat"], float):
        result["distance"] = haversine(lon, lat, result["lon"], result["lat"])
    else:
        del result

results.sort(key=lambda x: x["distance"], reverse=True)

print(results)