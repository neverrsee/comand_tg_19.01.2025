print("hello")
import telebot
from telebot import types
from hi import hi
from id import user_id
from Nikita import start
from buttons import links

bot = telebot.TeleBot("7307712996:AAHo1rZNud-Re5hKc1j98u0xRp6FBNtb0zk")

@bot.message_handler(commands=["start"])
def start_user(message):
    start(message, bot, types)

@bot.message_handler(commands=["button"])
def start_user(message):
    links(message, bot, types)

@bot.message_handler(commands=["hi", "hello"])
def hello(message):
    hi(message, bot)

@bot.message_handler(commands=["id"])
def user(message):
    user_id(message, bot)

bot.infinity_polling()

