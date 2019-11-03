from dotenv import load_dotenv
load_dotenv()

from flask import Flask, request, render_template, jsonify
app = Flask(__name__)

from src.attributes.weather import WeatherAttr
weatherAPI = WeatherAttr()

from src.attributes.osm import OSM
osmAPI = OSM()

from src.attributes.attr_get import Attributes
attributes = Attributes()

import os

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/api/attributes', methods=['GET'])
def get_attributes():
    return jsonify(attributes.get_attributes())

@app.route('/api/<attributes>', methods=['GET'])
def get_data(attributes):
    print(attributes)
    if attributes == 'weather':
        return {
            'data': weatherAPI.get_data(
                request.args.get('lat', 0),
                request.args.get('lon', 0),
                request.args.get('distance', 40),
                request.args.get('attribute', 'sun'))
            }
    else:
        return {
            'data': osmAPI.get_data(
                request.args.get('attribute', 'bread'),
                request.args.get('time', 0),
                request.args.get('lat', 0),
                request.args.get('lng', 0),
                request.args.get('distance', 40)
            )
        }


if __name__ == '__main__':
    app.run(debug=os.getenv('DEBUG_MODE', False), port=os.getenv('PORT', 5000))