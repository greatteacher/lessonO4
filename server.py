from datetime import datetime

from flask import Flask

from req import get_weather

city_id = 524901

apikey = '07535016bb8491634911732e9a804516'

app = Flask(__name__)

@app.route("/")
def index():
	url = "http://api.openweathermap.org/data/2.5/weather?id=%s&APPID=%s&units=metric" % (city_id, apikey)
	weather = get_weather(url)
	cur_date = datetime.now().strftime(' %A  %d %B')
	result = "<p> температура за бортом: %s </p>" % weather ['main']['temp']
	result += "<p>  <b> мы летим над городом: </b> %s </p>" % weather['name']
	result += "<p> Today is : %s </p>" % cur_date
	return result


if __name__=="__main__":
	app.run()


