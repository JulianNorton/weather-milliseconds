import datetime

import requests
from flask import Flask, render_template, request
from flask_caching import Cache
from htmlmin.minify import html_minify

app = Flask(__name__)

cache = Cache(config={'CACHE_TYPE': 'simple'})
cache.init_app(app)


@app.route('/')
@app.route('/index')
def index():

    timestamp = datetime.datetime.now()

    # // TODO -- MAKE THIS ACCEPT ANY LAT LONG AS A INPUT
    # latitude and Longitude and  of the area
    # NYC KNYC central park weather station is Lat: 40.78°N Lon: 73.97°W
    # long is not negative here because "TOP" in the request accounts for this.
    zip_code = request.args.get('zip_code')
    lat, lng, default_value = 0, 0, False
    with open('./assets/data.csv', 'r') as f:
        for line in f:
            data = line.split(',')
            if data[0] == zip_code:
                lat, lng = data[1], data[2].rstrip('\n')
                break

    if lat == 0 and lng == 0:
        lat, lng, default_value = 40.78, 73.97, True

    area_data = requests.get(
        f'https://api.weather.gov/points/{lat},{lng}'
    ).json()
    
    cwa, gridX, gridY = area_data['properties']['cwa'], area_data['properties']['gridX'], area_data['properties']['gridY']

    weather_data = requests.get(
        f'https://api.weather.gov/gridpoints/{cwa}/{gridX},{gridY}/forecast'
    ).json()

    periodic_data = weather_data['properties']['periods']

    areaDescription = area_data['properties']['relativeLocation']['properties']['city'] + ', ' + area_data['properties']['relativeLocation']['properties']['state'] +['',' (Default value)'][default_value]

    context = {
        'timestamp': timestamp,
        'periodic_data': periodic_data,
        'areaDescription': areaDescription
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
