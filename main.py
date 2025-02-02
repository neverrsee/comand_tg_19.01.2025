print("hello")
import telebot
from hi import hi, text_mess

bot = telebot.TeleBot("7307712996:AAHo1rZNud-Re5hKc1j98u0xRp6FBNtb0zk")

@bot.message_handler(commands=['hello'])
def text_hi(message):
    hi(message, bot)

@bot.message_handler(content_types=['text'])
def text_mess(message):
    text_mess(message, bot)

bot.infinity_polling()

