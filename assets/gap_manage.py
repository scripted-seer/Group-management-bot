import telebot

bot = telebot.TeleBot("token")

def get_admin_list(bot, chat_id):
    admins = bot.get_chat_administrators(chat_id)
    admin_list = []
        
    for admin in admins:
        user = admin.user
        full_name = user.first_name
        if user.last_name:
            full_name += " " + user.last_name
        if user.username:
            full_name += f" (@{user.username})"
        
        admin_list.append(full_name)
    
    return admin_list

@bot.message_handler(commands=['admins'])
def handle_admins(message):
    admins = get_admin_list(bot, message.chat.id)
    
    if admins:
        response = "لیست ادمین‌ها:\n" + "\n".join(admins)
    else:
        response = "خطا در دریافت لیست ادمین‌ها"
    
    return response


def ban(message):
    chat_id = message.chat.id
    user_id = message.reply_to_message.from_user.id
    name = message.reply_to_message.from_user.first_name

    member = bot.get_chat_member(chat_id, user_id) 
    if member.status in ["administrator", "creator"]: 
        return f" کاربر {name} ادمین است نمی‌توان او را بن کرد"
    
    bot.ban_chat_member(chat_id, user_id)
    return f" کاربر {name} از گروه بن شد"

def unban(message):
    chat_id = message.chat.id
    user_id = message.reply_to_message.from_user.id
    name = message.reply_to_message.from_user.first_name

    member = bot.get_chat_member(chat_id, user_id) 
    if member.status in ["administrator", "creator"]: 
        return f"هیچی دیگه کیرم تو مغزت"
    
    bot.unban_chat_member(chat_id, user_id)
    return f" کاربر {name} از گروه ان بن شد"


    
def mute(message):
    chat_id = message.chat.id
    user_id = message.reply_to_message.from_user.id
    name = message.reply_to_message.from_user.first_name

    member = bot.get_chat_member(chat_id, user_id) 
    if member.status in ["administrator", "creator"]: 
        return f" کاربر {name} ادمین است نمی‌توان او را سکوت کرد"
    
    bot.restrict_chat_member(
         chat_id, user_id,
         can_send_messages=False,  
         can_send_media_messages=False,  
         can_add_web_page_previews=False 
     )
    return f"{name} سکوت شد"

def unmute(message):
    chat_id = message.chat.id
    user_id = message.reply_to_message.from_user.id
    name = message.reply_to_message.from_user.first_name

    member = bot.get_chat_member(chat_id, user_id) 
    if member.status in ["administrator", "creator"]: 
        return f"کیرم تو مغزت"
    
    bot.restrict_chat_member(
         chat_id, user_id,
         can_send_messages=True,  
         can_send_media_messages=True,  
         can_add_web_page_previews=True 
     )
    return f"{name} از سکوت در اومد  "
def warn():
    pass
