

def hi(message, bot):
    bot.send_message(message.chat.id,"how are u")


def text_mess(message, bot):
    text = message.text.lower()
    if 'id' in text:
        bot.send_message(message.chat.id, f'your ID - {message.from_user.id}')
    elif 'username' in text:
        bot.send_message(message.chat.id, f'your ID - {message.from_user.username}')

