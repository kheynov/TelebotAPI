import telebot, time, random
token = 'Your token'
bot = telebot.TeleBot(token)
lastboot = time.asctime()

mon_lessons = ['''1.История
2.ОБЖ
3.Геометрия
4.Геометрия
5.Физика
6.Технопредпринимательство/Мехатроника. 
[3D прототипирование(пара)]''']

tue_lessons = ['''1.Алгебра
2.Алгебра
3.Химия
4.География
5.География
6.Русский язык
''']
wed_lessons = ['''1.Физ-ра
2.Инженерная графика
3.Англ.язык
4.Рус.яз
5.История
6.Лит-ра
7.Биология

ИЗ по инженерной графике
''']
thu_lessons = ['''1.География
2.Физика
3.Обществознание
4.Рус.яз
5.Литература
6.Англ.яз
7.Алгебра
''']

fri_lessons = ['''1.Алгебра
2.Алгебра
3.Биология
4.Физ-ра
5.ИЗО
6.Технопредпринимательство(2 группа)/Робототехника

ИЗ по инженерной графике
''']

sat_lessons = ['''1.Физика(ол.задачи)
2.Физика
3.Геометрия
4.Физ-ра
5.Химия
''']
print("initialised")
@bot.message_handler(commands=['start'])
def cmd_start(message):
	bot.send_message(message.chat.id, "Hello")
@bot.message_handler(commands=['sendsticker'])
def cmd_sendsticker(message):
	stickers = ["BQADAgADpQkAApI2owt3UnXTSkF3uwI", "BQADAgADswsAApI2owtg1HAfAvgjIgI", "BQADAgADTQADyJsDAAG6DcSDcxpKBAI", "BQADAgAD-QEAAtT-vgjZ7A86uU0H9gI", "BQADAgADZQADyJsDAAEoe0wLx8pmqAI", "BQADAgADaQADyJsDAAG3NoF1cpmzhQI", "BQADAgADOAADyIsGAAE7re09I3hMQwI"]
	bot.send_sticker(message.chat.id, stickers[random.randint(0, 6)])
@bot.message_handler(commands=['help'])
def cmd_help(message):
	bot.send_message(message.chat.id, "/time - Local time. /lastboot - last boot time. /sendsticker - send random sticker, /mondaylessons, /tuesdaylessons, /wednesdaylessons, /thursdaylessons, /fridaylessons, /saturdaylessons")
@bot.message_handler(commands=['lastboot'])	
def cmd_lastboot(message):
	bot.send_message(message.chat.id, lastboot)
@bot.message_handler(commands=['time'])
def cmd_time(message):
	bot.send_message(message.chat.id, time.asctime())
@bot.message_handler(commands=['mondaylessons'])
def cmd_monlessons(message):
	bot.send_message(message.chat.id, mon_lessons)
@bot.message_handler(commands=['tuesdaylessons'])
def cmd_tuelessons(message):
	bot.send_message(message.chat.id, tue_lessons)
@bot.message_handler(commands=['wednesdaylessons'])
def cmd_wedlessons(message):
	bot.send_message(message.chat.id, wed_lessons)
@bot.message_handler(commands=['thursdaylessons'])
def cmd_thulessons(message):
	bot.send_message(message.chat.id, thu_lessons)
@bot.message_handler(commands=['frilessons'])
def cmd_frilessons(message):
	bot.send_message(message.chat.id, fri_lessons)
@bot.message_handler(commands=['satlessons'])
def cmd_satlessons(message):
	bot.send_message(message.chat.id, sat_lessons)
if __name__ == '__main__':
	bot.polling(none_stop=True)
