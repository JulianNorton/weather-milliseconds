from app import app
from flask import render_template
from flask import json
from flask_caching import Cache


# Caching test 
# Check Configuring Flask-Caching section for more details
cache = Cache(app, config={'CACHE_TYPE': 'simple'})
@app.route('/cached')
@cache.cached(timeout=60)
def cached():
    return '''<html><body><h1>cached</h1></body></html>'''

# --------------



@app.route('/test')
def test():
    d = json.load(open('sample-forecast.json'))
    weather_formatted = d['data']['temperature'][0]
    # weather = {'sample_forecast': 'Always Sunny'}
    # return json.dumps(d)
    # return (weather=weather)
    # return render_template('index.html', title='Home', weather=weather, posts=posts)
    return '''<html>
    <head>
        <title>Home Page - Test</title>
    </head>
    <body>
        <p>{weather}</p>
        <p>{test}</p>
    </body>
</html>'''.format(weather=weather_formatted, test=d)

