import telebot

TOKEN = "8446961711:AAGIJ1O4yc9G2UMzK_oNe9dceXPbDMPvsyU"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(m):
    bot.reply_to(m, "سلام! ربات آماده است!")

bot.polling()
