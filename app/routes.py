from flask import render_template
from app import app
@app.route('/')
@app.route('/index')
def index():
    weather = {'forecast': 'Always Sunny', 'json': '''{
                "operationalMode":"Production",
                "srsName":"WGS 1984",
                "creationDate":"2018-03-09T11:21:00-05:00",
                "creationDateLocal":"9 Mar 13:51 pm EST",
                "productionCenter":"New York, NY",
                "credit":"http://weather.gov/okx/",
                "moreInformation":"http://weather.gov",
                "location":{
                    "region":"erh",
                    "latitude":"40.71",
                    "longitude":"-73.98",
                    "elevation":"26",
                    "wfo":"OKX",
                    "timezone":"E|Y|5",
                    "areaDescription":"New York NY",
                    "radar":"KDIX",
                    "zone":"NYZ072",
                    "county":"NYC061",
                    "firezone":"NYZ072",
                    "metar":"KNYC"
            },
                "time":{
                    "layoutKey":"k-p12h-n13-1",
                    "startPeriodName":[
                        "This Afternoon",
                        "Tonight",
                        "Saturday",
                        "Saturday Night",
                        "Sunday",
                        "Sunday Night",
                        "Monday",
                        "Monday Night",
                        "Tuesday",
                        "Tuesday Night",
                        "Wednesday",
                        "Wednesday Night",
                        "Thursday"
                    ],
                    "startValidTime":[
                        "2018-03-09T14:00:00-05:00",
                        "2018-03-09T18:00:00-05:00",
                        "2018-03-10T06:00:00-05:00",
                        "2018-03-10T18:00:00-05:00",
                        "2018-03-11T06:00:00-04:00",
                        "2018-03-11T18:00:00-04:00",
                        "2018-03-12T06:00:00-04:00",
                        "2018-03-12T18:00:00-04:00",
                        "2018-03-13T06:00:00-04:00",
                        "2018-03-13T18:00:00-04:00",
                        "2018-03-14T06:00:00-04:00",
                        "2018-03-14T18:00:00-04:00",
                        "2018-03-15T06:00:00-04:00"
                    ],
                    "tempLabel":["High","Low","High","Low","High","Low","High","Low","High","Low","High","Low","High"]
                },
                "data":{
                    "temperature":["43","32","44","31","43","33","40","32","40","30","40","30","42"],
                    "pop":["20",null,null,null,null,"30","40","30",null,null,null,null,null],
            
                    "weather":[
                        "Slight Chance Rain/Snow",
                        "Chance Sprinkles/Flurries then Partly Cloudy",
                        "Mostly Sunny",
                        "Mostly Clear",
                        "Sunny",
                        "Partly Cloudy then Chance Snow",
                        "Chance Snow then Chance Rain/Snow",
                        "Chance Snow",
                        "Partly Sunny",
                        "Partly Cloudy",
                        "Mostly Sunny",
                        "Partly Cloudy",
                        "Mostly Sunny"
                        ],
                    "iconLink":[
                        "http://forecast.weather.gov/newimages/medium/ra_sn20.png",
                        "http://forecast.weather.gov/DualImage.php?i=nra_sn&j=nsct&ip=10",
                        "http://forecast.weather.gov/newimages/medium/sct.png",
                        "http://forecast.weather.gov/newimages/medium/nfew.png",
                        "http://forecast.weather.gov/newimages/medium/few.png",
                        "http://forecast.weather.gov/DualImage.php?i=nsct&j=nsn&jp=30",
                        "http://forecast.weather.gov/DualImage.php?i=sn&j=ra_sn&ip=40&jp=40",
                        "http://forecast.weather.gov/newimages/medium/nsn30.png",
                        "http://forecast.weather.gov/newimages/medium/bkn.png",
                        "http://forecast.weather.gov/newimages/medium/nsct.png",
                        "http://forecast.weather.gov/newimages/medium/sct.png",
                        "http://forecast.weather.gov/newimages/medium/nsct.png",
                        "http://forecast.weather.gov/newimages/medium/sct.png"
                        ],
                    "hazard":[
            
                        ],
                    "hazardUrl":[
            
                        ],
                    "text":[
                        "A slight chance of rain and snow showers.  Mostly cloudy, with a high near 43. West wind around 17 mph.  Chance of precipitation is 20%.",
                        "A chance of sprinkles and flurries before 10pm, then a chance of flurries.  Mostly cloudy, with a low around 32. Wind chill values between 25 and 30. West wind 11 to 14 mph. ",
                        "Mostly sunny, with a high near 44. Wind chill values between 25 and 35. West wind 11 to 15 mph. ",
                        "Mostly clear, with a low around 31. Northwest wind 8 to 10 mph. ",
                        "Sunny, with a high near 43. Northwest wind 6 to 10 mph. ",
                        "A 30 percent chance of snow after 1am.  Mostly cloudy, with a low around 33.",
                        "A chance of snow before 1pm, then a chance of rain and snow.  Mostly cloudy, with a high near 40. Chance of precipitation is 40%.",
                        "A 30 percent chance of snow.  Mostly cloudy, with a low around 32.",
                        "Partly sunny, with a high near 40.",
                        "Partly cloudy, with a low around 30.",
                        "Mostly sunny, with a high near 40.",
                        "Partly cloudy, with a low around 30.",
                        "Mostly sunny, with a high near 42."			]
                    },
                    "currentobservation":{
                        "id":"KNYC",
                        "name":"New York City, Central Park",
                        "elev":"154",
                        "latitude":"40.78",
                        "longitude":"-73.97",
                        "Date":"9 Mar 13:51 pm EST",
                        "Temp":"41",
                        "Dewp":"21",
                        "Relh":"45",
                        "Winds":"13",
                        "Windd":"280",
                        "Gust":"25",
                        "Weather":"Mostly Cloudy",
                        "Weatherimage":"bkn.png",
                        "Visibility":"10.00",
                        "Altimeter":"1006.1",
                        "SLP":"29.74",
                        "timezone":"EST",
                        "state":"NY",
                        "WindChill":"34"
                    }
                }'''}
    
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', title='Home', weather=weather, posts=posts)