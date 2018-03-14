# Experiment to render the weather forecast as fast as possible. Goal is sub 100ms.

## Set-up

```
python3 -m venv venv && source venv/bin/activate && pip3 install -r requirements.txt && FLASK_APP=app.py FLASK_DEBUG=1 python -m flask run --port=5001
```


#### Good resources
* Setting up Flask: https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world


### Production setup

```
sudo python3 -m venv venv
source venv/bin/activate
sudo -H pip3 install -r requirements.txt
sudo FLASK_APP=app.py python3 -m flask run --port=5001
```

### Run forever
forever wasn't working, so I used a screen.

```
FLASK_APP=app.py start -c python3 app.py --port=5001
```

