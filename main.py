print("hello")
import telebot
from hi import hi


bot = telebot.TeleBot("7307712996:AAHo1rZNud-Re5hKc1j98u0xRp6FBNtb0zk")

@bot.message_handler(commands=["hi", "hello"])
def hello(message):
    hi(message, bot)

bot.infinity_polling()

