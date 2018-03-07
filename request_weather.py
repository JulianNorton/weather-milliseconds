from flask import Flask
import api_keys # TODO, handle enviromental secrets better. API key is stored here, not committed
# To CURL a URL
import requests

app = Flask(__name__)
noaa_api_key = noaa_api_key.api_keys
# TODO learn about flask config

@app.route('/')
def index():
    url = 'https://www.ncdc.noaa.gov/cdo-web/api/v2/locations?locationcategoryid=CITY&sortfield=name&sortorder=desc'
    headers = {'token': secret.api_key}
    r = requests.get(url, headers=headers)
    # python string format function
    
    return '''<html>
    <head>
        <title>Home Page - Test</title>
    </head>
    <body>
        <h1>{weather}</h1>
        <h2>{lightning}
    </body>
</html>'''.format(weather=str(r.json()),lightning='tacos')

# This has to be at bottom to run
if __name__ == '__main__':
    app.run()

# https://realpython.com/blog/python/api-integration-in-python/

# resp = requests.get('https://www.google.com')
# if resp.status_code != 200:
#     # This means something went wrong.
#     print('something went wrong')
# else:
#     print(resp)

# https://stackoverflow.com/questions/29927841/noaa-weather-rest-api-causes-error-when-requesting-with-curl
# curl -H "token:<token>" "https://www.ncdc.noaa.gov/cdo-web/api/v2/locations?locationcategoryid=CITY&sortfield=name&sortorder=desc"
