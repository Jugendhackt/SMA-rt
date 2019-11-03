import datetime
from math import radians, cos, sin, asin, sqrt

import requests


class OSM:
    def __init__(self):
        self.OVERPASS_URL = "https://lz4.overpass-api.de/api/interpreter"
        self.OSM_ID = 0

    def get_data(self, attribute: str, req_time: int, lat: float, lon: float, distance: int) -> dict:
        # self.check_date('timestring', req_time//1000)
        lat = float(lat)
        lon = float(lon)

        d = 2  # km
        lat1 = lat + d * (1 / 110.574)
        lon1 = lon + d * (1 / (111.320 * cos(lat)))
        lat0 = lat - d * (1 / 110.574)
        lon0 = lon - d * (1 / (111.320 * cos(lat)))
        print(lat0, lon0, lat1, lon1)

        overpass_query = f'''
        [out:json][timeout:25];
        (
        node["shop"="{OSM.get_parent_class(attribute)}"](48.289,9.803,48.474,10.26);
        );
        out body;
        '''

        response = requests.post(self.OVERPASS_URL, {'data': overpass_query})
        results = response.json()["elements"]

        for result in results:
            if isinstance(result["lon"], float) and isinstance(result["lat"], float):
                result["lng"] = result["lon"]
                result["distance"] = self.haversine(lon, lat, result["lon"], result["lat"])
                if result["distance"] <= distance:
                    del result
            else:
                del result

        results.sort(key=lambda x: x["distance"], reverse=False)
        return results

    @staticmethod
    def check_date(date_string: str, req_time: int) -> bool:
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

    @staticmethod
    def haversine(lon0, lat0, lon1, lat1):
        lon0, lat0, lon1, lat1 = map(radians, [lon0, lat0, lon1, lat1])
        dlon = lon1 - lon0
        dlat = lat1 - lat0
        a = sin(dlat / 2) ** 2 + cos(lat0) * cos(lat1) * sin(dlon / 2) ** 2
        c = 2 * asin(sqrt(a))
        r = 6371
        return c * r

    @staticmethod
    def get_parent_class(attribute):
        return {
            "bread": "bakery",
            "banana": "supermarket",
            "charging_cable": "mobile_phone",
        }[attribute.lower()]
