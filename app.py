from dotenv import load_dotenv
load_dotenv()

from flask import Flask, request, render_template
app = Flask(__name__)

from src.attributes.weather import WeatherAttr
weatherAPI = WeatherAttr()

import os

@app.route('/', methods=['GET'])
def index():
    return 'SMArt'
    # return render_template('index.html')


@app.route('/api/<int:key>', methods=['GET'])
def get_weather_data():
    if key == 0:
        return {
            'data': weatherAPI.get_data(
                request.args.get('lat', 0),
                request.args.get('lng', 0),
                request.args.get('distance', 40),
                request.args.get('weather', 'sun'))
            }
    else:
        return {}


if __name__ == '__main__':
    app.run(debug=os.getenv('DEBUG_MODE', False), port=os.getenv('PORT', 5000))