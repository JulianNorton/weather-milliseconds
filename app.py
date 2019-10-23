import datetime

import requests
from flask import Flask, render_template, request
from flask_caching import Cache
from htmlmin.minify import html_minify
from constants import CACHE_1_ZIP, CACHE_2_ZIP, CACHE_3_ZIP
import re

cache = Cache(config=
    {
        'CACHE_TYPE': 'simple',
        'CACHE_DEFAULT_TIMEOUT': 1800
    })

app = Flask(__name__)

cache.init_app(app)

def getContext(lat, lng, default_forecast, timestamp):
    area_data = requests.get(
        f'https://api.weather.gov/points/{lat},{lng}'
    ).json()
    
    cwa, gridX, gridY = area_data['properties']['cwa'], area_data['properties']['gridX'], area_data['properties']['gridY']

    weather_data = requests.get(
        f'https://api.weather.gov/gridpoints/{cwa}/{gridX},{gridY}/forecast'
    ).json()

    try:
        periodic_data = weather_data['properties']['periods']
    except:
        context = {
            'error': True,
            'title': weather_data['title'],
            'description': weather_data['detail']
        }
        return render_template('index.html', **context)

    areaDescription = area_data['properties']['relativeLocation']['properties']['city'] + ', ' + area_data['properties']['relativeLocation']['properties']['state'] +['',' (Default)'][default_forecast]

    context = {
        'timestamp': timestamp,
        'periodic_data': periodic_data,
        'areaDescription': areaDescription
    }

    return context

@app.route('/')
@app.route('/index')
@app.route('/<zip_code>')
def index(zip_code=None):
    
    timestamp = datetime.datetime.now()

    if zip_code != None and re.search(r'.*(\d{5}(\-\d{4})?)$', zip_code):
        if cache.get(CACHE_1_ZIP) is not None and cache.get(CACHE_1_ZIP)['zip_code'] == zip_code:
            return render_template('index.html', **cache.get(CACHE_1_ZIP)['context'])
        elif cache.get(CACHE_2_ZIP) is not None and cache.get(CACHE_2_ZIP)['zip_code'] == zip_code:
            return render_template('index.html', **cache.get(CACHE_2_ZIP)['context'])
        elif cache.get(CACHE_3_ZIP)  is not None and cache.get(CACHE_3_ZIP)['zip_code'] == zip_code:
            return render_template('index.html', **cache.get(CACHE_3_ZIP)['context'])
        else:
            lat, lng, default_value = 0, 0, False
            
            # zipcode-lat-lng.csv
            # https://gist.github.com/abatko/ee7b24db82a6f50cfce02afafa1dfd1e
            with open('./assets/zipcode-lat-lng.csv', 'r') as f:
                for line in f:
                    data = line.split(',')
                    if data[0] == zip_code:
                        lat, lng = data[1], data[2].rstrip('\n')
                        break
            
            if lat == 0 and lng == 0:
                context = {
                    'error': True,
                    'title': 'Something went wrong',
                    'description': 'We couldn\'t find information for the zipcode %s' %zip_code
                }
                return render_template('index.html', **getContext(lat, lng, False, timestamp))
            
            context = getContext(lat, lng, False, timestamp)

            data = {'zip_code': zip_code, 'context': context}

            def save_data(data):
                if cache.get(CACHE_1_ZIP) is None:
                    cache.set(CACHE_1_ZIP, data)
                    return
                elif cache.get(CACHE_2_ZIP) is None:
                    cache.set(CACHE_2_ZIP, data)
                    return
                elif cache.get(CACHE_3_ZIP) is None:
                    cache.set(CACHE_3_ZIP, data)
                    return

            save_data(data)

            return render_template('index.html', **context)
    else:
        #If no zip is provided, a default forecast is returned
        #New York, Manhattan, Central Park (default)
        return render_template('index.html', **getContext(40.76, -73.98, True, timestamp))




@app.after_request
def response_minify(response):
    '''
    minify html response to decrease site traffic
    '''
    if response.content_type == u'text/html; charset=utf-8':
        response.set_data(
            html_minify(response.get_data(as_text=True))
        )
        return response
    return response