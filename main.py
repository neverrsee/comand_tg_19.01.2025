print("hello")
import telebot
from telebot import types, bot, message
from buttons import links

bot = telebot.TeleBot("7307712996:AAHo1rZNud-Re5hKc1j98u0xRp6FBNtb0zk")

@bot.message_handler(commands='links')
def links(message):
    links(message, bot, types)


bot.infinity_polling()

