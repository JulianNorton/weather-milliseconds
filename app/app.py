from flask import Flask
from flask_caching import Cache
import os

cache = Cache(config={'CACHE_TYPE': 'simple'})

app = Flask(__name__)
cache.init_app(app)

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5001.
    port = int(os.environ.get('PORT', 5001))
    app.run(host='0.0.0.0', port=port)