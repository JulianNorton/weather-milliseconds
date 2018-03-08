from flask import Flask
import api_keys # TODO, handle enviromental secrets better. API key is stored here, not committed
# To CURL a URL
import requests


# Just webscrape instead?
# todo, https://forecast.weather.gov/MapClick.php?lat=40.7198&lon=-73.993&FcstType=digitalDWML
# https://forecast.weather.gov/MapClick.php?lat=40.7979&lon=-73.9664&unit=0&lg=english&FcstType=text&TextType=1

app = Flask(__name__)
noaa_api_key = ""
# TODO learn about flask config

url = "https://www.ncdc.noaa.gov/cdo-web/api/v2/datacategories?stationid=GHCND:USW00094728"
url = url + "&" "startdate=2018-01-01"
url = url + "&" "enddate=2018-01-02"

@app.route('/')
def index():
    # url = 'https://www.ncdc.noaa.gov/cdo-web/api/v2/locations?locationcategoryid=CITY&sortfield=name&sortorder=desc'
    headers = {'token': noaa_api_key}
    r = requests.get(url, headers=headers)
    # python string format function
    
    return '''<html>
    <head>
        <title>Home Page - Test</title>
    </head>
    <body>
        <p>{request}</p>
        <p>{weather}</p>
        <h2>{lightning}</h2>
    </body>
</html>'''.format(request=str(url), weather=str(r.json()),lightning='\n\n—')

# This has to be at bottom to run
if __name__ == '__main__':
    app.run()


"""
    {'metadata': {'resultset': {'offset': 1, 'count': 5, 'limit': 25}}, 'results': [{'name': 'Computed', 'id': 'COMP'}, {'name': 'Precipitation', 'id': 'PRCP'}, {'name': 'Air Temperature', 'id': 'TEMP'}, {'name': 'Wind', 'id': 'WIND'}, {'name': 'Weather Type', 'id': 'WXTYPE'}]}
"""
# resp = requests.get('https://www.google.com')
# if resp.status_code != 200:
#     # This means something went wrong.
#     print('something went wrong')
# else:
#     print(resp)

# https://stackoverflow.com/questions/29927841/noaa-weather-rest-api-causes-error-when-requesting-with-curl
# curl -H "token:<token>" "https://www.ncdc.noaa.gov/cdo-web/api/v2/locations?locationcategoryid=CITY&sortfield=name&sortorder=desc"
