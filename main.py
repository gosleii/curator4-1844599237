import telebot

bot = telebot.TeleBot('7490470344:AAFiMvzbJ0FuydDVB0nKFo7zOWeQpLZVdNc')


@bot.message_handler(commands=['start'])
def start_handler(message):
    bot.send_message(message.chat.id, '*Напиши  цикл с параметром*')


@bot.message_handler(commands=['for'])
def for_handker(message):
    bot.send_message(message.chat.id, '_Напиши  цикл пока_', parse_mode='Markdown')


@bot.message_handler(commands=['while'])
def while_handker(message):
    bot.send_message(message.chat.id, '[Узнай больше на сайте](https://pythontutor.ru/lessons/for_loop/)',
                     parse_mode='Markdown')


bot.infinity_polling()