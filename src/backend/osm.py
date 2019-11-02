import requests
import json

osm_response = requests.get("https://nominatim.openstreetmap.org/reverse?format=json&lat=48.4&lon=9.98")

overpass_url = "https://overpass-api.de/api/interpreter"
overpass_query = """
[out:json][timeout:25];
area(""" + str(osm_response.json()["osm_id"]) + """)->.searchArea;
(
  node["shop"="bakery"](area.searchArea);
);
out body;
"""

response = requests.post(overpass_url, {'data': overpass_query})

#data = response.json()
print(response.json())