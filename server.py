from datetime import datetime

from flask import Flask
from all_news_list import all_news
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

@app.route("/news/<int:news_id>")
def news_by_id(news_id):
	# date = date.strftime(' %m %Y %B') попыталась дату формат поменять.. надо подумать как
	news_to_show = [news for news in all_news if news['id'] == news_id]
	# return 'Новость:  ' + str(news_id) # сделали строкой, попросили только число выводить
	if len(news_to_show) == 1:
		# print(news_to_show) # выводил новость 
		result = "<h1>%(title)s</h1><p><i>%(date)s</i></p><p><b>%(text)s</i></b>"
		result = result % news_to_show[0]
		return 'Новость:  %s' % result # новость загала в ковычки, заменив подстановокой, т.е. %
	else: 
		abort(404)



if __name__=="__main__":
	app.run(port=5010)      # если что, d скобках стереть порт равен 5010 или использовать что-то другое, автоматически использует 5000


