from flask import Flask
from flask_caching import Cache
import os

cache = Cache(config={'CACHE_TYPE': 'simple'})

app = Flask(__name__)
cache.init_app(app)

if __name__ == '__main__':
    app.run(
        host=app.config.get("HOST", "localhost"),
        port=app.config.get("PORT", 5001)
    )