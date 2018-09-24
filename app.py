from flask import Flask
from flask import render_template
from flask import json
from flask_caching import Cache

import datetime
import requests

app = Flask(__name__)

cache = Cache(config={'CACHE_TYPE': 'simple'})
cache.init_app(app)

@app.route('/')
@app.route('/index')

# 1800 seconds == 30 minutes
@cache.cached(timeout=1800)
def index():
    timestamp = datetime.datetime.now()
    raw_data = requests.get('https://forecast.weather.gov/MapClick.php?lat=40.74&lon=-74&unit=0&lg=english&FcstType=json').json()
    # raw_data = json.load(open('sample-forecast.json'))
    parsed_data = {
        'areaDescription' : raw_data['location']['areaDescription'],
        'forecast_time' : raw_data['time']['startPeriodName'][0],
        'forecast_data_weather' : raw_data['data']['weather'][0],
        'forecast_data_text' : raw_data['data']['text'][0],
        'forecast_time_1' : raw_data['time']['startPeriodName'][1],
        'forecast_data_weather_1' : raw_data['data']['weather'][1],
        'forecast_data_text_1' : raw_data['data']['text'][1],
        'forecast_time_2' : raw_data['time']['startPeriodName'][2],
        'forecast_data_weather_2' : raw_data['data']['weather'][2],
        'forecast_data_text_2' : raw_data['data']['text'][2],
        'forecast_time_3' : raw_data['time']['startPeriodName'][3],
        'forecast_data_weather_3' : raw_data['data']['weather'][3],
        'forecast_data_text_3' : raw_data['data']['text'][3],
        'forecast_data_weather_4' : raw_data['data']['weather'][4],
        'forecast_data_text_4' : raw_data['data']['text'][4]
    }
    return render_template('index.html',timestamp=timestamp, **parsed_data)
