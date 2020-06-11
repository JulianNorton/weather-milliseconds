# Experiment to render the weather forecast as fast as possible. ~~Goal is sub 100ms.~~ ~40 milliseconds if you're in NYC.

## https://weather.juliannorton.com

## Set-up

```
python3 -m venv venv && source venv/bin/activate && pip3 install -r requirements.txt && FLASK_APP=app.py FLASK_DEBUG=1 python -m flask run --port=5001
```


#### Good resources
* Setting up Flask: https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world


### Production setup

```
# Use a screen
# [not needed after venv installed] sudo python3 -m venv venv
screen
source venv/bin/activate
sudo -H pip3 install -r requirements.txt
sudo FLASK_APP=app.py python3 -m flask run --port=5001
```
`Ctrl a` `p` to detatch from the screen 

### Production reset

```
(To find python processes:)
ps -ef | grep python
sudo kill -9 23826
("23826" is whatever the number is returned that you want to kill)
screen
sudo git pull
sudo python3 -m venv venv
source venv/bin/activate
sudo -H pip3 install -r requirements.txt
sudo FLASK_APP=app.py python3 -m flask run --port=5001
```
