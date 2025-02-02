print("hello")
import telebot
import id

bot = telebot.TeleBot("7307712996:AAHo1rZNud-Re5hKc1j98u0xRp6FBNtb0zk")

player = []

@bot.message_handler(commands=["id"])
def info(message):
    id.user_id(message, bot)


bot.infinity_polling()

