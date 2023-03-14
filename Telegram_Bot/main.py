import telebot
from extensions import ConversionException, Converter
from config import keys, TOKEN


bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['help'])
def send_help(message):
    bot.send_message(message.chat.id, "Отправьте сообщение в формате: "
                                      "\n<перевести из> <перевести в> <сумма>"
                                      "\nПример: доллар рубль 100.75"
                                      "\nУвидеть список доступных валют: /values")

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, f"Привет, {message.chat.username}!")
    send_help(message)

@bot.message_handler(commands=['values'])
def send_values(message):
    text = 'Доступные валюты:'
    for key in keys.keys():
        text = '\n'.join((text, key, ))
    bot.send_message(message.chat.id, text)

@bot.message_handler(content_types=['text'])
def convert(message: telebot.types.Message):
    try:
        values = message.text.lower().split(' ')

        if len(values) != 3:
            raise ConversionException(f'Введено неверное число параметров:\n{len(values)} вместо 3-х')

        quote, base, amount = values
        result = Converter.get_price(quote, base, amount)
    except ConversionException as e:
        bot.reply_to(message, f'Ошибка пользователя.\n{e}.')
    except Exception as e:
        bot.reply_to(message, f'Не удалось обработать команду.\n{e}.')
    else:
        bot.send_message(message.chat.id, f'{amount} {keys[quote]} = {result} {keys[base]}')


bot.polling(none_stop=True)