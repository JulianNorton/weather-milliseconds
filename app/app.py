from flask import Flask
import requests # to curl a URL
import json # process sample json

# TODO learn about flask config


# Import sample json data, #TODO, load dynamically and cache
with open('sample-forecast.json') as json_data:
    sample_forecast = json.load(json_data)


app = Flask(__name__)


# This has to be at bottom to run
if __name__ == '__main__':
    app.run()




# notes
# resp = requests.get('https://www.google.com')
# if resp.status_code != 200:
#     # This means something went wrong.
#     print('something went wrong')
# else:
#     print(resp)
