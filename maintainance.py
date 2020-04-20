import telebot
import config

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(func=lambda x: True)
def reply(message):
    bot.reply_to(message, "sorry, bot is currently under maintainance")

bot.polling(none_stop=True)
