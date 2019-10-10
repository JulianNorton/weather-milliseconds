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


    # // TODO -- MAKE THIS ACCEPT ANY LAT LONG AS A INPUT
    # latitude and Longitude and  of the area
    # NYC KNYC central park weather station is Lat: 40.78°N Lon: 73.97°W
    # long is not negative here because "TOP" in the request accounts for this.
    # latitude, longitude = 40.73, -73.97

    # Fetching area data
    # area_data = requests.get(
    #    f'https://api.weather.gov/points/40.73,-73.97'
    # ).json()

    # print(area_data)

    # Fetching weather data
    # Hardcoding to the correct weather station
    weather_data = requests.get(
        f'https://api.weather.gov/gridpoints/OKX/33,35/forecast'
    ).json()

    # Period wise data
    periodic_data = weather_data['properties']['periods']

    context = {
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
