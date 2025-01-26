

text = ""

def user_id(message, bot):
    # создать переменную для хранения айди пользователя
    user_id = message.chat.id
    print(message)
    text = message.chat.id()
    if "id" in text:
        bot.sed_message(message.chat.id, f"You ID: {message.from_user.id}")
    # бот отправит сообщение человеку с айди пользователя
