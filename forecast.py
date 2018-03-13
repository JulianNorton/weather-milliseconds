from app import app
from flask import render_template
from flask import json
from flask_caching import Cache
import datetime
import requests



cache = Cache(app, config={'CACHE_TYPE': 'simple'})
timestamp = datetime.datetime.now()
@app.route('/manhattan')
# 600 seconds == 10 minutes
@cache.cached(timeout=600)
def manhattan():
    raw_data = requests.get('https://forecast.weather.gov/MapClick.php?lat=40.74&lon=-74&unit=0&lg=english&FcstType=json').json()
    # raw_data = json.load(open('sample-forecast.json'))
    areaDescription = raw_data['location']['areaDescription']
    creationDateLocal = raw_data['creationDateLocal']
    forecast_time = raw_data['time']['startPeriodName'][0]
    forecast_data_weather = raw_data['data']['weather'][0]
    forecast_data_text = raw_data['data']['text'][0]
    return '''<html>
    <body>
        <h5>Compiled: {timestamp}</h5>
        <p>{areaDescription} – {creationDateLocal}</p>
        <h3>{forecast_time} – {forecast_data_weather}</h3>
        <p>{forecast_data_text}</p>
        <hr/>
        <p>{raw_data}</p>
    </body>
</html>'''.format(
    timestamp=timestamp,
    areaDescription=areaDescription,
    creationDateLocal=creationDateLocal,
    forecast_time=forecast_time,
    forecast_data_weather=forecast_data_weather,
    forecast_data_text=forecast_data_text,
    raw_data=raw_data)

