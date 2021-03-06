import os
from time import gmtime, strftime

import requests


class WeatherAttr:
    def __init__(self):
        self.URL = os.getenv('WEATHER_URL')

    def get_data(self, lat: float, lng: float, distance: int, weather: str) -> list:
        if weather not in ['rain', 'sun', 'snow', 'wind', 'storm'] or distance < 0:
            return list()
        cur_date = strftime("%y-%m-%d", gmtime())
        params = {
            'action': 'request',
            'lng': lng, 'lat': lat,
            'weather': weather,
            'date': cur_date,
            'distance': distance,
            'params': '{"maximumTemperature":140,"minimumTemperature":-76,"snowAccumulation":0,"cloudCover":1,'
                      '"minimumWindSpeed"`:12} '
        }
        r = requests.post(self.URL, params)
        return r.json()['places']
