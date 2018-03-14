from flask import Flask
from flask import render_template
from flask import json
from flask_caching import Cache

import datetime
import requests

app = Flask(__name__)

cache = Cache(config={'CACHE_TYPE': 'simple'})
cache.init_app(app)


cache = Cache(app, config={'CACHE_TYPE': 'simple'})

@app.route('/')
@app.route('/index')

# 600*6 seconds == 30 minutes
@cache.cached(timeout=600*3)
def index():
    timestamp = datetime.datetime.now()
    raw_data = requests.get('https://forecast.weather.gov/MapClick.php?lat=40.74&lon=-74&unit=0&lg=english&FcstType=json').json()
    # raw_data = json.load(open('sample-forecast.json'))
    parsed_data = {
        'areaDescription' : raw_data['location']['areaDescription'],
        'creationDateLocal' : raw_data['creationDateLocal'],
        'forecast_time' : raw_data['time']['startPeriodName'][0],
        'forecast_data_weather' : raw_data['data']['weather'][0],
        'forecast_data_text' : raw_data['data']['text'][0]
    }
    return render_template('index.html',timestamp=timestamp, raw_data=raw_data, **parsed_data)