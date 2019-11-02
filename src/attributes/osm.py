# Just for testing without Flask app:
from dotenv import load_dotenv
load_dotenv()

import requests
import os
import datetime
import calendar

class OSM:
    def __init__():
        self.OVERPASS_URL = "https://overpass-api.de/api/interpreter"
        self.OSM_ID = 0

    def get(req_time: int) -> dict:
        self.parse_date('timestring', req_time//1000)
        return ''

    def parse_date(date_string: str, req_time: int) -> :
        date = datetime.datetime.fromtimestamp(req_time)
        days = ['Mo', 'Tu', 'We', 'Th', 'Fr', 'Sa', 'Su']
        opening_entries = date_string.split(';')
        for entry in opening_entries:
            split_days, split_hours = entry.split(' ')
            if len(split_days) > 2:
                d1, d2 = split_days.split('-')
                
            else:







