from flask import Flask
from flask_caching import Cache
import os

cache = Cache(config={'CACHE_TYPE': 'simple'})

app = Flask(__name__)
cache.init_app(app)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)