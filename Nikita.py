def start(message,bot,types):
    markup = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton("Киберспорт", url='https://www.cybersport.ru/')
    markup.add(button1)
    print(message)
    bot.send_message(message.chat.id, f"Привет, {message.from_user}! Нажми на кнопку и перейди на сайт)", reply_markup=markup)
