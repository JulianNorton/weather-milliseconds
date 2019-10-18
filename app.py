import datetime

import requests
from flask import Flask, render_template, request
from flask_caching import Cache
from htmlmin.minify import html_minify

cache = Cache(config=
    {
        'CACHE_TYPE': 'simple',
        'CACHE_DEFAULT_TIMEOUT': 1800
    })

app = Flask(__name__)

cache.init_app(app)

@app.route('/')
@app.route('/index')
@app.route('/<zip_code>')
def index(zip_code=None):

    if cache.get(zip_code):
        return render_template('index.html', **cache.get(zip_code))
    else:

        timestamp = datetime.datetime.now()

        lat, lng, default_value = 0, 0, False

        if zip_code is None:
            zip_code, default = 10019, True #New York, Manhattan, Central Park (default)

        with open('./assets/data.csv', 'r') as f:
            for line in f:
                data = line.split(',')
                if data[0] == zip_code:
                    lat, lng = data[1], data[2].rstrip('\n')
                    break

        if lat == 0 and lng == 0:
            lat, lng, default_value = 40.76, -73.98, True

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

        cache.set(zip_code, context)

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
