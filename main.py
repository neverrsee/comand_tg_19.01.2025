from telebot import types
import telebot
from hi import hi, text_mess
import Nikita
from buttons import links

bot = telebot.TeleBot("7307712996:AAHo1rZNud-Re5hKc1j98u0xRp6FBNtb0zk")

player = []

@bot.message_handler(commands=["id"])
def info(message):
    id.user_id(message, bot)


@bot.message_handler(commands=['hello'])
def text_hi(message):
    hi(message, bot)


@bot.message_handler(commands='links')
def links(message):
    links(message, bot, types)

@bot.message_handler(commands=['start'])
def buttons_start(message):
    Nikita.start(message,bot,types)

@bot.message_handler(content_types=['text'])
def text_mess(message):
    text_mess(message, bot)

bot.infinity_polling()

