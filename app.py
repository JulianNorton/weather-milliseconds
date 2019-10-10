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

    timestamp = datetime.datetime.now()

    # latitude and Longitude and  of the area
    latitude, longitude = 41, 74

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
