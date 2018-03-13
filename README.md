# Experiment to render the weather forecast as fast as possible. Goal is sub 100ms.

## Set-up

```
python3 -m venv venv && source venv/bin/activate && pip3 install -r requirements.txt && FLASK_APP=forecast.py FLASK_DEBUG=1 python3 -m flask run
```


#### Good resources
* Setting up Flask: https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world


### Production setup

```
sudo -H pip3 install -r requirements.txt
```

