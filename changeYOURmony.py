import telebot
from config import TOKEN,keys
from extensions import Convertor, ConverterException




bot = telebot.TeleBot(TOKEN)
@bot.message_handler(commands=['start', 'help'])
def start(message: telebot.types.Message):
    text = 'Hallo! Ich kann dir helfen! ' \
           'Ich kann deinen gewünschten Betrag in die gewünschte Währung konvertieren.' \
           ' Lass uns starten, geben Sie die folgenden Werte ein:' \
           '\n<Währung><konvertierte Währung><Betrag>' \
           '\n Verfügbare Währung, klick hier: /values'
    bot.reply_to(message, text)


@bot.message_handler(commands=['values'])
def values(message:telebot.types.Message):
    text = 'Verfügbare Währung:'
    for key in keys.keys():
       text = '\n'.join((text,key,))
    bot.reply_to(message,text)

@bot.message_handler(content_types=['text'])
def converter(message:telebot.types.Message):
    values= message.text.split()
    values = list(map(str.lower,values))
    try:
        result = Convertor.get_price(values)
    except ConverterException as e:
        bot.reply_to(message, f'Benutzerfehler!\n{e}')
    except Exception as e:
        bot.reply_to(message, f'der Befehl kann nicht ausgeführt werden!\n{e}')
    else:
        text = f'Preis {values[0]} {values[2]} -- {result} {keys[values[1]]}'
        bot.reply_to(message,text)

bot.polling(none_stop=True, interval=0)
