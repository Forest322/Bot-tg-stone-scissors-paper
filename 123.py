from telebot import TeleBot
from telebot import types
import random

TOKEN = '7505424553:AAH-gnl9ZaxiISnOE2OukqAKePcWWy4GZL8'

bot = TeleBot(TOKEN)

v = ['✂️','📄','🧱']
a = ''

kb = types.ReplyKeyboardMarkup(row_width=3)
kb.row('✂️','📄','🧱')

@bot.message_handler(commands=['start'])
def hendle_start(message: types.Message):
    global a
    a = v[random.randint(0, 2)]
    print(a)
    bot.send_message(message.chat.id, 'Привет! Один из смаликов ✂️ 📄 🧱', reply_markup=kb)

@bot.message_handler(content_types=['text'])
def hendle_start(message: types.Message): 
    global a    
    text = message.text
    print(a)
    print(text)
    if not a:
        bot.send_message(message.chat.id, 'Нажми /start для следущий игры')
        return
    elif text != '✂️' and text != '📄' and text != '🧱':
        bot.send_message(message.chat.id, 'Только один из смаликов ✂️ 📄 🧱')
        return
    elif a == '✂️' and text == '🧱':
        bot.send_message(message.chat.id, 'Вы выйграли, нажми /start для следущий игры')
    elif a == '📄' and text == '✂️':
        bot.send_message(message.chat.id, 'Вы выйграли, нажми /start для следущий игры')
    elif a == '🧱' and text == '📄':
        bot.send_message(message.chat.id, 'Вы выйграли, нажми /start для следущий игры')
    elif a == '🧱' and text == '✂️':
        bot.send_message(message.chat.id, 'Вы проиграли, нажми /start для следущий игры')
    elif a == '✂️' and text == '📄':
        bot.send_message(message.chat.id, 'Вы проиграли, нажми /start для следущий игры')
    elif a == '📄' and text == '🧱':
        bot.send_message(message.chat.id, 'Вы проиграли, нажми /start для следущий игры')   
    elif a == text:
        bot.send_message(message.chat.id, 'Ничя, нажи /start для следущий игры')   
    bot.send_message(message.chat.id, f'У кампютера было {a}') 
    a = ''


print('Сервер запущен')
bot.polling(non_stop=True, interval=1)