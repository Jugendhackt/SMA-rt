from dotenv import load_dotenv
load_dotenv()

import os

from flask import Flask, request
app = Flask(__name__, static_url_path='/src/frontend')
from src.attributes.weather import WeatherAttr

weatherAPI = WeatherAttr()

@app.route('/', methods=['GET'])
def index():
    return ''

@app.route('/weather', methods=['GET'])
def get_weather_data():
    return {
        'data': weatherAPI.get_data(
            request.args.get('lat', 0),
            request.args.get('lng', 0),
            request.args.get('distance', 40),
            request.args.get('weather', 'sun'))
        }


if __name__ == '__main__':
    app.run(debug=os.getenv('DEBUG_MODE', False), port=os.getenv('PORT', 5000))