import telebot
from telebot import types

# ====== توکن ربات ======
TOKEN = "8446961711:AAGIJ1O4yc9G2UMzK_oNe9dceXPbDMPvsyU"
bot = telebot.TeleBot(TOKEN)

# ======= دکمه اصلی =======
def main_keyboard():
    kb = types.InlineKeyboardMarkup()
    kb.add(types.InlineKeyboardButton("خدمات", callback_data="services"))
    kb.add(types.InlineKeyboardButton("نمونه‌کارها", callback_data="portfolio"))
    kb.add(types.InlineKeyboardButton("رضایت", callback_data="feedback"))
    kb.add(types.InlineKeyboardButton("راهنما و قوانین", callback_data="rules"))
    kb.add(types.InlineKeyboardButton("پشتیبانی", callback_data="support"))
    return kb

# ======= دکمه های خدمات =======
def services_keyboard():
    kb = types.InlineKeyboardMarkup()
    kb.add(types.InlineKeyboardButton("لوگو", callback_data="service_logo"))
    kb.add(types.InlineKeyboardButton("پست اینستاگرام", callback_data="service_post"))
    kb.add(types.InlineKeyboardButton("کاور یوتیوب", callback_data="service_cover"))
    kb.add(types.InlineKeyboardButton("بازگشت", callback_data="back"))
    return kb

# ======= دستور شروع =======
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "سلام! یکی از گزینه‌های زیر را انتخاب کن:", reply_markup=main_keyboard())

# ======= هندل دکمه ها =======
@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    chat_id = call.message.chat.id
    
    # ===== خدمات =====
    if call.data == "services":
        bot.edit_message_text(chat_id=chat_id, message_id=call.message.message_id,
                              text="کدوم خدمت مورد نظرت هست؟", reply_markup=services_keyboard())

    # ===== توضیحات خدمات =====
    elif call.data.startswith("service_"):
        service_name = call.data.split("_")[1]
        descriptions = {
            "logo": "خدمت طراحی لوگو: لوگو حرفه‌ای برای برند شما",
            "post": "خدمت طراحی پست اینستاگرام: پست جذاب و حرفه‌ای",
            "cover": "خدمت طراحی کاور یوتیوب: کاور با طراحی اختصاصی"
        }
        text = descriptions.get(service_name, "توضیح موجود نیست")
        
        # دکمه سفارش + برگشت
        kb = types.InlineKeyboardMarkup()
        kb.add(types.InlineKeyboardButton("سفارش", callback_data=f"order_{service_name}"))
        kb.add(types.InlineKeyboardButton("بازگشت", callback_data="services"))
        
        bot.edit_message_text(chat_id=chat_id, message_id=call.message.message_id,
                              text=text, reply_markup=kb)

    # ===== ثبت سفارش =====
    elif call.data.startswith("order_"):
        service_name = call.data.split("_")[1]
        bot.send_message(chat_id, f"کاربر محترم، لطفاً توضیحات سفارش {service_name} خودت رو بنویس:")
        
        # ذخیره وضعیت سفارش کاربر
        user_orders[chat_id] = service_name

    # ===== بازگشت به خدمات =====
    elif call.data == "back":
        bot.edit_message_text(chat_id=chat_id, message_id=call.message.message_id,
                              text="کدوم خدمت مورد نظرت هست؟", reply_markup=services_keyboard())

    # ===== بقیه گزینه های اصلی =====
    elif call.data == "portfolio":
        bot.edit_message_text(chat_id=chat_id, message_id=call.message.message_id,
                              text="نمونه‌کارها:\n1. لوگو\n2. پست اینستاگرام\n3. کاور یوتیوب",
                              reply_markup=main_keyboard())
    elif call.data == "feedback":
        bot.edit_message_text(chat_id=chat_id, message_id=call.message.message_id,
                              text="رضایت مشتری‌ها: همه راضی بودن 😎", reply_markup=main_keyboard())
    elif call.data == "rules":
        bot.edit_message_text(chat_id=chat_id, message_id=call.message.message_id,
                              text="قوانین ربات:\n1. احترام\n2. رعایت زمان‌بندی\n3. پرداخت صحیح",
                              reply_markup=main_keyboard())
    elif call.data == "support":
        bot.edit_message_text(chat_id=chat_id, message_id=call.message.message_id,
                              text="برای پشتیبانی با @YourUsername تماس بگیر", reply_markup=main_keyboard())

# ======= دریافت پیام کاربر برای سفارش =======
user_orders = {}  # دیکشنری برای ذخیره وضعیت سفارش هر کاربر

@bot.message_handler(func=lambda m: m.chat.id in user_orders)
def handle_order_text(message):
    service_name = user_orders.pop(message.chat.id)
    bot.send_message(message.chat.id,
                     f"ممنون! توضیحات سفارش {service_name} دریافت شد.\nما با شما تماس می‌گیریم.")

# ======= شروع ربات =======
bot.polling()
