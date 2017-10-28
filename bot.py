import telebot
import random
import json
import requests
with open('config.json') as file:
	data = json.load(file)
	token = data["token"]
	stickers = data["stickers"]
	comm = data["help_commands"]
	id = data["Accepted_id"]
	unknown_comm = data["unknown_comm"]

req = requests.get('http://api.openweathermap.org/data/2.5/weather?q=Novosibirsk&appid=d10fc51ddd8a8cf366007d95febf16bc')
timeurl = requests.get('http://time.jsontest.com')
timejson = timeurl.json()
time = timejson['time']

dataParced = req.json()
temp = float(dataParced['main']['temp']) - 273.15
humid = dataParced['main']['humidity']
wind = dataParced['wind']['speed']
bot = telebot.TeleBot(token)
print("initialised")

@bot.message_handler(content_types=['text'])
def get_message(message):
	if message.chat.id == id:
		if message.text == "/help":
			bot.send_message(message.chat.id, comm)
		elif message.text == "/weather":
			req=requests.get('http://api.openweathermap.org/data/2.5/weather?q=Novosibirsk&appid=d10fc51ddd8a8cf366007d95febf16bc')
			dataParced = req.json()
			temp = float(dataParced['main']['temp']) - 273.15
			humid = dataParced['main']['humidity']
			wind = dataParced['wind']['speed']
			weather = "Погода: " + str(temp) + " C\n" + "Влажность: " + str(humid) + "%\n" + "Скорость ветра: " + str(wind)+"м/с\n"
			bot.send_message(id, weather)
		elif  message.text == "/send_sticker":
			bot.send_sticker(id, stickers[random.randint(0,6)])
		elif message.text == "/time":
			req = requests.get('http://api.openweathermap.org/data/2.5/weather?q=Novosibirsk&appid=d10fc51ddd8a8cf366007d95febf16bc')
			timeurl = requests.get('http://time.jsontest.com')
			timejson = timeurl.json()
			time = timejson['time']
			bot.send_message(id, time)
		else:
			bot.send_sticker(id, unknown_comm[random.randint(0, 4)])
	else:
			bot.send_message(message.chat.id, "Вы не правы, всего доброго!")
			bot.send_sticker(message.chat.id, unknown_comm[random.randint(0, 4)])
if time == "11:00:00 AM":
	req = requests.get('http://api.openweathermap.org/data/2.5/weather?q=Novosibirsk&appid=d10fc51ddd8a8cf366007d95febf16bc')
	dataParced = req.json()
	temp = float(dataParced['main']['temp']) - 273.15
	humid = dataParced['main']['humidity']
	wind = dataParced['wind']['speed']
	weather = "Погода: " + str(temp) + " C\n" + "Влажность: " + str(humid) + "%\n" + "Скорость ветра: " + str(wind) + "м/с\n"
	Ya_Begu_I_Pukau = "Доброе утро, \%username\%! \n" + weather
	bot.send_message(id, Ya_Begu_I_Pukau)

if __name__ == '__main__':
	bot.polling(none_stop=True)
