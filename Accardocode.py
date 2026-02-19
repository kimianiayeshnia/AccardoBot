import telebot

TOKEN = "توکنتو اینجا بذار"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(m):
    bot.reply_to(m, "سلام! ربات آماده است!")

bot.polling()
