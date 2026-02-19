import telebot

# ====== اینجا توکن رباتتو بذار ======
TOKEN = "8446961711:AAGIJ1O4yc9G2UMzK_oNe9dceXPbDMPvsyU"
bot = telebot.TeleBot(TOKEN)

# ======= دستور شروع =======
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "سلام! خوش اومدی به ربات طراحی من. نمونه‌کارها و سفارشات رو می‌تونی اینجا ببینی.")

# ======= نمایش نمونه‌کار ساده =======
@bot.message_handler(commands=['portfolio'])
def show_portfolio(message):
    bot.send_message(message.chat.id, "نمونه‌کار 1: لوگو\nنمونه‌کار 2: پست اینستاگرام\nنمونه‌کار 3: کاور یوتیوب")

# ======= ثبت سفارش ساده =======
@bot.message_handler(commands=['order'])
def order_design(message):
    bot.send_message(message.chat.id, "لطفاً نوع سفارش و توضیحاتت رو بفرست:")

# ======= دریافت پیام کاربر =======
@bot.message_handler(func=lambda m: True)
def echo_all(message):
    bot.send_message(message.chat.id, f"پیام شما دریافت شد: {message.text}\nبعداً با شما تماس می‌گیریم.")

# ======= شروع ربات =======
bot.polling()
