import datetime

import requests
from flask import Flask, render_template
from flask_caching import Cache
from htmlmin.minify import html_minify

app = Flask(__name__)

cache = Cache(config={'CACHE_TYPE': 'simple'})
cache.init_app(app)


@app.route('/')
@app.route('/index')
@cache.cached(timeout=300)  # 1800 seconds == 30 minutes
def index():

    # raw_data = requests.get('https://forecast.weather.gov/MapClick.php?lat=40.74&lon=-74&unit=0&lg=english&FcstType=json').json()
    # raw_data = json.load(open('sample-forecast.json'))

    # data = raw_data['data']
    # time_data = raw_data['time']

    # parsed_data = {
    #     'areaDescription': raw_data['location']['areaDescription'],

    #     'forecast_time': time_data['startPeriodName'][0],
    #     'forecast_data_weather': data['weather'][0],
    #     'forecast_data_text': data['text'][0],

    #     'forecast_time_1': time_data['startPeriodName'][1],
    #     'forecast_data_weather_1': data['weather'][1],
    #     'forecast_data_text_1': data['text'][1],

    #     'forecast_time_2': time_data['startPeriodName'][2],
    #     'forecast_data_weather_2': data['weather'][2],
    #     'forecast_data_text_2': data['text'][2],

    #     'forecast_time_3': time_data['startPeriodName'][3],
    #     'forecast_data_weather_3': data['weather'][3],
    #     'forecast_data_text_3': data['text'][3],

    #     'forecast_data_weather_4': data['weather'][4],
    #     'forecast_data_text_4': data['text'][4]
    # }

    timestamp = datetime.datetime.now()

    # latitude and Longitude and  of the area
    latitude, longitude = 31, 80

    # Fetching area data
    area_data = requests.get(
       f'https://api.weather.gov/points/{latitude},{longitude}'
    ).json()

    # if the area data is available
    try:
        area_description = area_data['properties']['relativeLocation']['properties']['city']

    # if the area data is not available for the provided point
    except KeyError:
        area_description = ''

    # Fetching weather data
    weather_data = requests.get(
        f'https://api.weather.gov/gridpoints/TOP/{latitude},{longitude}/forecast'
    ).json()

    # Period wise data
    periodic_data = weather_data['properties']['periods']

    context = {
        'areaDescription': area_description,
        'timestamp': timestamp,
        'periodic_data': periodic_data
    }

    return render_template('index.html', **context)


@app.after_request
def response_minify(response):
    """
    minify html response to decrease site traffic
    """
    if response.content_type == u'text/html; charset=utf-8':
        response.set_data(
            html_minify(response.get_data(as_text=True))
        )

        return response
    return response
