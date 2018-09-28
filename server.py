from datetime import datetime

from flask import Flask

from req import get_weather

import settings

city_id = 524901

app = Flask(__name__)

@app.route("/")
def index():
	url = "http://api.openweathermap.org/data/2.5/weather?id=%s&APPID=%s&units=metric" % (city_id, settings.API_KEY)
	weather = get_weather(url)
	cur_date = datetime.now().strftime(' %A  %d %B')
	result = "<p> Tемпература за бортом: %s </p>" % weather ['main']['temp']
	result += "<p>  <b> Mы летим над городом: </b> %s </p>" % weather['name']
	result += "<p> Today is : %s </p>" % cur_date
	return result


if __name__=="__main__":
	app.run(port=5010)      # если что, d скобках стереть порт равен 5010 или использовать что-то другое, автоматически использует 5000


