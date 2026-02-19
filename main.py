import telebot
from telebot import types

TOKEN = "8446961711:AAGIJ1O4yc9G2UMzK_oNe9dceXPbDMPvsyU"
bot = telebot.TeleBot(TOKEN)

# ======= کیبورد اصلی زیر باکس پیام =======
def main_keyboard():
    kb = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    kb.add("🦋 خدمات 🪼", "نمونه‌کارها")
    kb.add("‼️ رضایت 💘", "راهنما و قوانین")
    kb.add("📢 پشتیبانی و مشاوره قبل از خرید")
    return kb

# ======= دکمه های شیشه ای خدمات =======
def services_inline():
    kb = types.InlineKeyboardMarkup(row_width=2)

    kb.add(
        types.InlineKeyboardButton("طراحی رابط کاربری وبسایت", callback_data="ui"),
        types.InlineKeyboardButton("طراحی لوگو", callback_data="logo")
    )

    kb.add(
        types.InlineKeyboardButton("طراحی کارت ویزیت", callback_data="card"),
        types.InlineKeyboardButton("طراحی سربرگ", callback_data="letterhead")
    )

    kb.add(
        types.InlineKeyboardButton("طراحی بروشور", callback_data="brochure"),
        types.InlineKeyboardButton("طراحی پوستر", callback_data="poster")
    )

    kb.add(
        types.InlineKeyboardButton("طراحی تراکت", callback_data="flyer"),
        types.InlineKeyboardButton("طراحی ست اداری", callback_data="setedari")
    )

    kb.add(
        types.InlineKeyboardButton("طراحی منوی رستوران", callback_data="menu"),
        types.InlineKeyboardButton("طراحی کاراکتر دوبعدی", callback_data="character")
    )

    kb.add(
        types.InlineKeyboardButton("طراحی کاور موزیک", callback_data="music"),
        types.InlineKeyboardButton("طراحی کاور کتاب", callback_data="book")
    )

    kb.add(
        types.InlineKeyboardButton("طراحی پست اینستاگرام", callback_data="insta"),
        types.InlineKeyboardButton("پیاده سازی روی موکاپ", callback_data="mockup")
    )

    kb.add(
        types.InlineKeyboardButton("بازگشت", callback_data="back_to_main")
    )

    return kb


# ======= دستور /start =======
@bot.message_handler(commands=['start'])
def start_msg(message):
    bot.send_message(message.chat.id,
"""به دنیای خدمات گرافیکی آکاردو خوش اومدی💭🪷

🪽طراحی سفارشی و متناسب با نیازهای شما 
🪽استفاده از رنگها و اشکال منحصر به فرد
🪽تحویل به موقع و با کیفیت بالا
🪽مشاوره رایگان برای انتخاب بهترین طرح

✨ همین الن سفارشت رو ثبت کن و اولین قدم برای موفقیت برندت رو بردار!

🐚 انجام تمام خدمات گرافیکی 🎳""",
                     reply_markup=main_keyboard())

# ======= هندل پیام های اصلی (ReplyKeyboard) =======
@bot.message_handler(func=lambda m: True)
def handle_main(message):
    chat_id = message.chat.id
    text = message.text

    if text == "🪼 خدمات":
        bot.send_message(chat_id, """🩷 لطفا خدمات مورد نظر خود را انتخاب کنید:

🖊 استفاده از این ربات به منزله قبول تمامی قوانین ربات هست.
⚜ قوانین: /rules:""", reply_markup=services_inline())
    elif text == "🦋 نمونه‌کارها":
        bot.send_message(chat_id, """برای مشاهده نمونه‌کارهای انجام‌شده و آشنایی با سبک طراحی‌ها،
از طریق لینک زیر وارد گالری بشید و با خیال راحت انتخاب کنید 👇""",
                         reply_markup=main_keyboard())
    elif text == "💘 رضایت":
        bot.send_message(chat_id, """⭐ اعتماد ساخته نمی‌شود، اثبات می‌شود.

بازخورد مشتری‌های ما، گواه کیفیت، دقت و تعهد در هر پروژه است.

برای مشاهده رضایت‌ها و نظرات ثبت‌شده، از طریق لینک زیر اقدام کنید 👇""", reply_markup=main_keyboard())
    elif text == "‼️ راهنما و قوانین":
        bot.send_message(chat_id, """📜 قوانین ثبت سفارش

 لطفاً قبل از ثبت سفارش، توضیحات کامل و دقیق پروژه را ارسال کنید.
 پس از نهایی شدن جزئیات، زمان تحویل اعلام می‌شود و رعایت خواهد شد.
 شروع طراحی پس از تأیید سفارش انجام می‌شود.
 امکان ویرایش جزئی وجود دارد، اما تغییرات کلی شامل هزینه جداگانه خواهد بود.
 پس از تحویل نهایی و تأیید مشتری، پروژه بسته خواهد شد.
 ارسال فایل نهایی پس از تسویه انجام می‌شود.
 احترام متقابل در طول همکاری الزامی است 🤍

✨ ثبت سفارش به منزله مطالعه و پذیرش قوانین است.""",
                         reply_markup=main_keyboard())
    elif text == "📢 پشتیبانی و مشاوره قبل از خرید":
        bot.send_message(chat_id, """📞 پشتیبانی و مشاوره قبل از ثبت سفارش

اگر برای انتخاب نوع طراحی یا جزئیات پروژه‌تون سوالی دارید،
قبل از ثبت سفارش می‌تونید مشاوره رایگان دریافت کنید.

ما کمک می‌کنیم بهترین انتخاب رو متناسب با نیاز و بودجه‌تون داشته باشید 🤍

برای ارتباط مستقیم از طریق آیدی زیر پیام بدید 👇
@YourUsername""", reply_markup=main_keyboard())

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
while True:
    try:
        bot.polling(none_stop=True)
    except Exception as e:
        print("Error:", e)

