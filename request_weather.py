from flask import Flask
import api_keys # TODO, handle enviromental secrets better. API key is stored here, not committed
# To CURL a URL
import requests

app = Flask(__name__)
noaa_api_key = ""
# TODO learn about flask config

@app.route('/')
def index():
    url = 'https://www.ncdc.noaa.gov/cdo-web/api/v2/locations?locationcategoryid=CITY&sortfield=name&sortorder=desc'
    headers = {'token': noaa_api_key}
    r = requests.get(url, headers=headers)
    # python string format function
    
    return '''<html>
    <link href="https://cdn.jsdelivr.net/npm/tailwindcss/dist/tailwind.min.css" rel="stylesheet">
    <head>
        <title>Home Page - Test</title>
    </head>
    <body>
        <p>{weather}</p>
        <h2>{lightning}</h2>
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
