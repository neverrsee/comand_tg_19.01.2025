def user_id(message, bot):
    # создать переменную для хранения айди пользователя
    user_id = message.chat.id
    print(message)
    text = message.chat.id()
    if "id" in text:
        bot.sed_message(message.chat.id, f"You ID: {message.from_user.id}")
    # бот отправит сообщение человеку с айди пользователя

def answer(call, types, bot):
    if call.data == "yes":
        markup_reply = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn_id = types.KeyboardButton("ID")
        markup_reply.add(btn_id)
        bot.send_message(call.message.chat.id, "Выбериб что тебе интересует")