import telebot
import config
bot = telebot.TeleBot(config.tok)
def start_(mes):
    bot.send_message(mes.chat.id, "Приветствую!")
    #заменить "..." на команды#
    bot.send_message(mes.chat.id, "команды:\n"
                                  "*/...\n"
                                  "*/...\n"
                                  "*/...\n"
                                  "*/...\n"
                                  "*/...\n"
                                  "*/...")