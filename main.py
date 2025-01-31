print("hello")
import telebot
from start import start_

bot = telebot.TeleBot("7307712996:AAHo1rZNud-Re5hKc1j98u0xRp6FBNtb0zk")

def start_go(message):
    start_(message)


bot.infinity_polling()