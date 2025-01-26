from telebot import types

def links(message, bot):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Далее')
    btn2 = types.KeyboardButton('Ссылки')
    btn3 = types.KeyboardButton('Клинки!')
    markup.add(btn1, btn2, btn3)
    bot.send_message(message.user.id, "Выбери кнопку!", reply_markup=markup)


def check(message, bot):
    if message.text == 'Далее':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)  # создание новых кнопок
        btn1 = types.KeyboardButton('Бу, испугался?')
        btn2 = types.KeyboardButton('Убежать')
        markup.add(btn1, btn2)
    elif message.text == 'Cсылки':
        bot.send_message(message.user.id,"Наш проект на гитхабе" + "[Github](https://github.com/neverrsee/comand_tg_19.01.2025)", parse_mode='Markdown')
    elif message.text == 'Кликни!':
        bot.send_message(message.user.id, )




