import requests

def get_weather(url):
		result = requests.get(url)
		if result.status_code==200:
			return result.json() # вместо 2 и 3 пункта
		# print(result.text)  # 1. печататет как текст, заменили 2 пунктом
		# print(result.json())  # 2. печатает как dict словарь, дикшионэри
		# print(result.json()['name'])  # 3. печатает как элемент  словаря, а именно имя города Moscow 
		else:
			print('что-то пошло не так, Хьюстен, у нас проблемы')



if __name__=="__main__":
	# get_weather("http://api.openweathermap.org/data/2.5/weather?q=Moscow&APPID=07535016bb8491634911732e9a804516")
	# добавим дата в начале строки и принт этой дата
	data = get_weather("http://api.openweathermap.org/data/2.5/weather?id=524901&APPID=07535016bb8491634911732e9a804516&units=metric")
	print(data)