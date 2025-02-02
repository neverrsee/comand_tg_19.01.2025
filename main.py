print("hello")
import telebot
import buttons
import Nikita
from telebot import types

bot = telebot.TeleBot("7307712996:AAHo1rZNud-Re5hKc1j98u0xRp6FBNtb0zk")

@bot.message_handler(commands=['start'])
def buttons_start(message):
    Nikita.start(message,bot,types)

bot.infinity_polling()

