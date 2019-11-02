# Just for testing without Flask app:
from dotenv import load_dotenv
load_dotenv()

import requests
import os
import datetime
import calendar
import requests
import json
from math import radians, cos, sin, asin, sqrt

class OSM:
    def __init__(self):
        self.OVERPASS_URL = "https://lz4.overpass-api.de/api/interpreter"
        self.OSM_ID = 0

    def get_data(self, attribute: str, req_time: int, lat: float, lon: float, distance: int) -> dict:
        # self.check_date('timestring', req_time//1000)

        range = 60 # km
        lat1 = float(lat) + range * (1 / 110.574)
        lon1 = float(lon) + range * (1 / (111.320 * cos(lat)))
        lat0 = float(lat) - range * (1 / 110.574)
        lon0 = float(lon) - range * (1 / (111.320 * cos(lat)))

        overpass_query = f'''
        [out:json][timeout:25];
        (
        node["shop"="{attribute}"]({lat0},{lon0},{lat1},{lon1});
        );
        out body;
        '''

        response = requests.post(self.OVERPASS_URL, {'data': overpass_query})
        results = response.json()["elements"]

        for result in results:
            if isinstance(result["lon"], float) and isinstance(result["lat"], float):
                result["distance"] = self.haversine(lon, lat, result["lon"], result["lat"])
                if result["distance"] <= distance:
                    del result
            else:
                del result

        results.sort(key=lambda x: x["distance"], reverse=False)
        return results

    def check_date(self, date_string: str, req_time: int) -> bool:
        date = datetime.datetime.fromtimestamp(req_time)
        days = ['Mo', 'Tu', 'We', 'Th', 'Fr', 'Sa', 'Su']
        opening_entries = date_string.split(';')
        for entry in opening_entries:
            split_days, split_hours = entry.split(' ')
            if len(split_days) > 2:
                d1, d2 = split_days.split('-')
                return True
            else:
                return False

    def haversine(self, lon0, lat0, lon1, lat1):
        lon0, lat0, lon1, lat1 = map(radians, [lon0, lat0, lon1, lat1])
        dlon = lon1 - lon0 
        dlat = lat1 - lat0 
        a = sin(dlat/2)**2 + cos(lat0) * cos(lat1) * sin(dlon/2)**2
        c = 2 * asin(sqrt(a)) 
        r = 6371
        return c * r
