from dotenv import load_dotenv
load_dotenv()

from flask import Flask, request, render_template
app = Flask(__name__)

from src.attributes.weather import WeatherAttr
weatherAPI = WeatherAttr()

from src.attributes.osm import OSM
osmAPI = OSM()

import os

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/api/<attributes>', methods=['GET'])
def get_data(attributes):
    if attributes == 0:
        return {
            'data': weatherAPI.get_data(
                request.args.get('lat', 0),
                request.args.get('lng', 0),
                request.args.get('distance', 40),
                request.args.get('weather', 'sun'))
            }
    else:
        return {
            'data': osmAPI.get_data(
                request.args.get('attribute', 'bakery'),
                request.args.get('time', 0),
                request.args.get('lat', 0),
                request.args.get('lng', 0),
                request.args.get('distance', 40)
            )
        }


if __name__ == '__main__':
    app.run(debug=os.getenv('DEBUG_MODE', False), port=os.getenv('PORT', 5000))