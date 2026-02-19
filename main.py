import telebot
from telebot import types

TOKEN = "8446961711:AAGIJ1O4yc9G2UMzK_oNe9dceXPbDMPvsyU"
bot = telebot.TeleBot(TOKEN)

# ======= کیبورد اصلی زیر باکس پیام =======
def main_keyboard():
    kb = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    kb.add("خدمات", "نمونه‌کارها")
    kb.add("رضایت", "راهنما و قوانین")
    kb.add("پشتیبانی")
    return kb

# ======= دکمه های شیشه ای خدمات =======
def services_inline():
    kb = types.InlineKeyboardMarkup()
    kb.add(types.InlineKeyboardButton("لوگو", callback_data="service_logo"))
    kb.add(types.InlineKeyboardButton("پست اینستاگرام", callback_data="service_post"))
    kb.add(types.InlineKeyboardButton("کاور یوتیوب", callback_data="service_cover"))
    kb.add(types.InlineKeyboardButton("بازگشت", callback_data="back_to_main"))
    return kb

# ======= دستور /start =======
@bot.message_handler(commands=['start'])
def start_msg(message):
    bot.send_message(message.chat.id,
                     "سلام! یکی از گزینه‌های زیر را انتخاب کن:",
                     reply_markup=main_keyboard())

# ======= هندل پیام های اصلی (ReplyKeyboard) =======
@bot.message_handler(func=lambda m: True)
def handle_main(message):
    chat_id = message.chat.id
    text = message.text

    if text == "خدمات":
        bot.send_message(chat_id, "خدمات ما:", reply_markup=services_inline())
    elif text == "نمونه‌کارها":
        bot.send_message(chat_id, "نمونه‌کارها:\n1. لوگو\n2. پست اینستاگرام\n3. کاور یوتیوب",
                         reply_markup=main_keyboard())
    elif text == "رضایت":
        bot.send_message(chat_id, "رضایت مشتری‌ها: همه راضی 😎", reply_markup=main_keyboard())
    elif text == "راهنما و قوانین":
        bot.send_message(chat_id, "قوانین ربات:\n1. احترام\n2. رعایت زمان‌بندی\n3. پرداخت صحیح",
                         reply_markup=main_keyboard())
    elif text == "پشتیبانی":
        bot.send_message(chat_id, "برای پشتیبانی با @YourUsername تماس بگیر", reply_markup=main_keyboard())

# ======= هندل دکمه های شیشه ای خدمات =======
user_orders = {}

@bot.callback_query_handler(func=lambda call: True)
def handle_services(call):
    chat_id = call.message.chat.id
    if call.data.startswith("service_"):
        service_name = call.data.split("_")[1]
        descriptions = {
            "logo": "طراحی لوگو حرفه‌ای برای برند شما",
            "post": "طراحی پست اینستاگرام جذاب و حرفه‌ای",
            "cover": "طراحی کاور یوتیوب اختصاصی"
        }
        text = descriptions.get(service_name, "توضیح موجود نیست")
        # دکمه سفارش + بازگشت
        kb = types.InlineKeyboardMarkup()
        kb.add(types.InlineKeyboardButton("سفارش", callback_data=f"order_{service_name}"))
        kb.add(types.InlineKeyboardButton("بازگشت", callback_data="back_to_services"))
        bot.edit_message_text(chat_id=chat_id, message_id=call.message.message_id,
                              text=text, reply_markup=kb)
    elif call.data.startswith("order_"):
        service_name = call.data.split("_")[1]
        bot.send_message(chat_id, f"کاربر محترم، لطفاً توضیحات سفارش {service_name} خودت رو بنویس:")
        user_orders[chat_id] = service_name
    elif call.data == "back_to_services":
        bot.edit_message_text(chat_id=chat_id, message_id=call.message.message_id,
                              text="خدمات ما:", reply_markup=services_inline())
    elif call.data == "back_to_main":
        bot.edit_message_text(chat_id=chat_id, message_id=call.message.message_id,
                              text="یکی از گزینه‌های زیر را انتخاب کن:", reply_markup=main_keyboard())

# ======= دریافت توضیحات سفارش =======
@bot.message_handler(func=lambda m: m.chat.id in user_orders)
def handle_order_text(message):
    service_name = user_orders.pop(message.chat.id)
    bot.send_message(message.chat.id,
                     f"ممنون! توضیحات سفارش {service_name} دریافت شد.\nما با شما تماس می‌گیریم.",
                     reply_markup=main_keyboard())

# ======= شروع ربات =======
bot.polling()
