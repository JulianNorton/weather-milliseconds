from flask import Flask
app = Flask(__name__)

# API key is stored here, not committed
import secret

@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()


# To CURL a URL
import requests

noaa_api_key = secret.api_key()

print(noaa_api_key)

# https://realpython.com/blog/python/api-integration-in-python/

# resp = requests.get('https://www.google.com')
# if resp.status_code != 200:
#     # This means something went wrong.
#     print('something went wrong')
# else:
#     print(resp)

# https://stackoverflow.com/questions/29927841/noaa-weather-rest-api-causes-error-when-requesting-with-curl
# curl -H "token:<token>" "https://www.ncdc.noaa.gov/cdo-web/api/v2/locations?locationcategoryid=CITY&sortfield=name&sortorder=desc"
