import telebot
import config
from assets import normal_message, api, gap_manage

bot = telebot.TeleBot(config.token)

@bot.message_handler(func=lambda message: message.text and 'راهنما' in message.text.lower())
def send_hello_message(message):
    bot.reply_to(message, api.help())

@bot.message_handler(func=lambda message: message.text and 'سلام' in message.text.lower())
def send_hello_message(message):
    bot.reply_to(message, normal_message.hello_message())

@bot.message_handler(func=lambda message: any(word in message.text.lower() for word in ["شب بخیر","شب خوش","شبتون بخیر","شبتون خوش"]))
def send_gn_message(message):
    bot.reply_to(message, normal_message.good_night())

@bot.message_handler(func=lambda message: any(word in message.text.lower() for word in ["صبح بخیر","صبح خوش","صبحتون بخیر","صبحتون خوش"]))
def send_gn_message(message):
    bot.reply_to(message, normal_message.good_morning())

@bot.message_handler(func=lambda message: message.text and 'حوصلم' in message.text.lower())
def send_hello_message(message):
    bot.reply_to(message, normal_message.normalitation_message())

@bot.message_handler(func=lambda message: message.text and 'داستان' in message.text.lower())
def send_mini_story(message):
    bot.reply_to(message, api.mini_story())

@bot.message_handler(func=lambda message: message.text and 'پروکسی' in message.text.lower())
def send_mini_story(message):
    bot.reply_to(message, api.proxy())

@bot.message_handler(func=lambda message: message.text and 'دانستنی' in message.text.lower())
def send_mini_story(message):
    bot.reply_to(message, api.danestani())

@bot.message_handler(func=lambda message: message.text and 'اطلاعات دارو' in message.text.lower())
def send_mini_story(message):
    bot.reply_to(message, "نام دارو رو به صورت کامل و واضح بدون غلط املایی وارد کن (کاندوم ماندوم نخوای ها)")
    bot.register_next_step_handler(message, get_name)
def get_name(message):
    name = message.text
    bot.reply_to(message, api.daroo(name))

@bot.message_handler(func=lambda message: message.text and 'دیالوگ' in message.text.lower())
def send_mini_story(message):
    bot.reply_to(message, api.dialog())

@bot.message_handler(func=lambda message: message.text and 'فال' in message.text.lower())
def send_mini_story(message):
    bot.send_photo(message.chat.id, api.fal(), caption="فال شما : هرچند زندگیت مثل قیافته ولی خب بخونش امیدوار بشی ")

@bot.message_handler(func=lambda message: message.text and 'اوقات شرعی' in message.text.lower())
def send_mini_story(message):
    bot.reply_to(message, "کدوم شهر ؟")
    bot.register_next_step_handler(message, get_name_oghat)
def get_name_oghat(message):
    name = message.text
    bot.reply_to(message, api.oghat_shari(name))

@bot.message_handler(func=lambda message: message.text and 'دریافت لیست ادمین' in message.text.lower())
def show_admins(message):
    bot.reply_to(message, gap_manage.handle_admins(message))

@bot.message_handler(func=lambda message: message.text and message.text.strip().lower() == "بن")
def ban_user(message):
    bot.reply_to(message, gap_manage.ban(message))

@bot.message_handler(func=lambda message: message.text and message.text.strip().lower() == "حذف بن")
def ban_user(message):
    bot.reply_to(message, gap_manage.unban(message))

@bot.message_handler(func=lambda message: message.text and message.text.strip().lower() == "سکوت")
def ban_user(message):
    bot.reply_to(message, gap_manage.mute(message))

@bot.message_handler(func=lambda message: message.text and message.text.strip().lower() == "حذف سکوت")
def ban_user(message):
    bot.reply_to(message, gap_manage.unmute(message))

    
bot.infinity_polling()
