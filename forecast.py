from app import app
from flask import render_template
from flask import json
from flask import jsonify
# from pprint import pprint




@app.route('/test')
def test():
    d = json.load(open('sample-forecast.json'))
    weather_formatted = d['data']['temperature'][0]
    jsonify
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

