import telebot
from telebot import types
import json
import datetime
import time
bot = telebot.TeleBot('6945939631:AAHKk5f5fHOvpnFZu9QRkGpBKBQeOzvVlYA')
bot_id = '@MrAdarshG_746'
check_list =['@Pro_CoderZ','@DILCHABOYOFFICIAL','@Lifafa_Zones','@ZDILCHAGIVEAWAYZ','@star_Giveawa','@TgBots_PayOuTs','@Dilchaboysofficial']
bonamount = float(1)
def get_data(file_name):
    try:
        with open(file_name, 'r') as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        return None
    except Exception as e:
        return None

# Function to save data to a file
def save_data(file_name, data):
    try:
        with open(file_name, 'w') as file:
            json.dump(data, file)
        return True
    except Exception as e:
        return False
def get_balance(chat_id):
    file_name = f'{bot_id}-{chat_id}-balance.json'  # Specify the fixed file name format
    data = get_data(file_name)
    if data and 'balance' in data:
        return data['balance']
    else:
        return 0
def add_balance(chat_id, amount):
    file_name = f'{bot_id}-{chat_id}-balance.json'
    data = get_data(file_name)
    if data and 'balance' in data:
        data['balance'] += amount  # Add the amount to the existing balance
    else:
        data = {'balance': amount}  # If no existing data, create a new entry with the provided amount
    if save_data(file_name, data):
        return True
    else:
        return False
# Get the current date and time
current_time = datetime.datetime.now()

# Format the current time as a string
formatted_date = current_time.strftime("%d-%m-%Y")
formatted_time = current_time.strftime("%H:%M:%S")

Developer_keyboard = types.InlineKeyboardMarkup()
Sos_button = types.InlineKeyboardButton(text="🇮🇳 Dᴇᴠᴇʟᴏᴘᴇʀ", url="https://t.me/MrAdarshG")
Developer_keyboard.add(Sos_button)

bot_status = None
per_refer = 1
payout = "GoogleCard_PayOuT"
earn_text = f"<b>🔰 Pʟᴇᴀꜱᴇ Fᴇᴇʟ Fʀᴇᴇ Tᴏ Rᴇᴀᴄʜ Oᴜᴛ Tᴏ Oᴜʀ Sᴜᴘᴘᴏʀᴛ Tᴇᴀᴍ, Iꜰ Yᴏᴜ Hᴀᴠᴇ Aɴʏ Qᴜᴇꜱᴛɪᴏɴꜱ Oʀ Iꜱꜱᴜᴇꜱ.\n\n😎 Iꜰ Yᴏᴜ Hᴀᴠᴇ Tʜᴇɴ Cʟɪᴄᴋ Oɴ Tʜᴇ Bᴇʟᴏᴡ Bᴜᴛᴛᴏɴ.</b>"
ytchannel = f"""<a  href="https://youtube.com/@Pro_Coderz?si=95eO-cCk1SCehBNY">么 𝐘ᴛ 𝐂ʜᴀɴɴᴇʟ = @𝐏ʀᴏ𝐂ᴏᴅᴇʀ𝐙 么</a>"""

Channel_keyboard = types.InlineKeyboardMarkup()

# Line 1
channels_buttons_line1 = [
    types.InlineKeyboardButton(text="Pᴄ [ Rᴇᴅɪʀᴇᴄᴛ ] ❤️", url="https://t.me/Pro_CoderZ"),
    types.InlineKeyboardButton(text="Tᴄ [ Rᴇᴅɪʀᴇᴄᴛ ] 🎉", url="https://t.me/DILCHABOYOFFICIAL")
]
Channel_keyboard.add(*channels_buttons_line1)

# Line 2
channels_buttons_line2 = [
    types.InlineKeyboardButton(text="Rᴄɢ [ Rᴇᴅɪʀᴇᴄᴛ ] 🛒", url="https://t.me/Dilchaboysofficial"),types.InlineKeyboardButton(text="Oʜ [ Rᴇᴅɪʀᴇᴄᴛ ] 💸", url="https://t.me/+vYQSPc7zIchkZWQ0")
]
Channel_keyboard.add(*channels_buttons_line2)

# Line 3
channels_buttons_line3 = [
    types.InlineKeyboardButton(text="Lᴢ [ Rᴇᴅɪʀᴇᴄᴛ ] 🤞", url="https://t.me/Lifafa_Zones"),
    types.InlineKeyboardButton(text="Sɢ [ Rᴇᴅɪʀᴇᴄᴛ ] 🥳", url="https://t.me/+GXrcL-_yz-9kMTVl")
]
Channel_keyboard.add(*channels_buttons_line3)

# Line 5
channels_buttons_line5 = [
    types.InlineKeyboardButton(text="Sɢ [ Rᴇᴅɪʀᴇᴄᴛ ] 🚀", url="https://t.me/star_giveawa"),
    types.InlineKeyboardButton(text="Ds [ Rᴇᴅɪʀᴇᴄᴛ ] 😍", url="https://t.me/+CqYKNQFOaxcxZDBl")
]
Channel_keyboard.add(*channels_buttons_line5)

# Line 7
channels_buttons_line7 = [
    types.InlineKeyboardButton(text="Ls [ Rᴇᴅɪʀᴇᴄᴛ ] 🖤", url="https://t.me/+Kf8BpGZOWaQwNzI1"),
    types.InlineKeyboardButton(text="Zɢ [ Rᴇᴅɪʀᴇᴄᴛ ] 💙", url="https://t.me/ZDILCHAGIVEAWAYZ")
]
Channel_keyboard.add(*channels_buttons_line7)


# Line 6
channels_buttons_line6 = [
    types.InlineKeyboardButton(text="TɢBᴏᴛs PᴀʏOᴜT ↗️", url=f"https://t.me/{payout}")
]
Channel_keyboard.add(*channels_buttons_line6)

# Replace 'YOUR_API_TOKEN' with the provided bot token
keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
keyboard.row("🟢 Joined")

@bot.message_handler(commands=['start'])
def handle_start(message):
    broadcast = get_data(f"{bot_id}-user_id.json")
    if broadcast == None:
        push = []
    else:
        push = broadcast

    check_user = push.count(message.from_user.id)
    if check_user > 0:
         """user_exist"""
    else:
        push.append(message.from_user.id)
        save_data(f"{bot_id}-user_id.json", push)
    check = get_data(f'{bot_id}-{message.from_user.id}-refer.json')
    if check == None:
        if message.text != '/start':
    	    refer = message.text.split( )[1]
    	    if str(refer) == str(message.from_user.id):
    	    	refer = "@None"    	    	
    	    	
        else:
        	refer = "@None"
        hi = save_data(f'{bot_id}-{message.from_user.id}-refer.json',refer)
        hi = get_data(f'{bot_id}-{message.from_user.id}-refer.json')
        try:
        	msg = f"""<a href="tg://user?id={message.chat.id}">{message.from_user.first_name}</a>"""
        	bot.send_message(refer,f'<b>🚧 Nᴇᴡ Uꜱᴇʀ Oɴ Yᴏᴜʀ ɪɴᴠɪᴛᴇ Lɪɴᴋ: {msg}</b>',parse_mode='HTML')
        except:
        	save_data(f'{bot_id}-{message.from_user.id}-refer.json','@None')       	
  #  bot.send_message(message.chat.id,hi)
    user_id = message.chat.id
    try:
        bot.send_photo(user_id,photo="https://t.me/Bots_Pay_Alert/880",caption=f"""<b>⛔ Mᴜꜱᴛ Jᴏɪɴ Oᴜʀ Aʟʟ ᴄʜᴀɴɴᴇʟs\n\n{ytchannel}</b>""", reply_markup=Channel_keyboard, parse_mode='HTML')
        bot.send_message(user_id,f"""<b>✅ Aꜰᴛᴇʀ  Jᴏɪɴɪɴɢ Aʟʟ Cʜᴀɴɴᴇʟs, Cʟɪᴄᴋ Oɴ '🟢 Jᴏɪɴᴇᴅ'</b>""", reply_markup=keyboard, parse_mode='HTML')
    except Exception as e:
        bot.send_message(user_id, f"An error occurred: {e}")

@bot.message_handler(func=lambda message: message.text == '🟢 Joined')
def handle_joined_message(message):
    check = True
    for i in check_list:
        try:
            status = bot.get_chat_member(user_id=message.from_user.id, chat_id=i)
        except:
             bot.send_message( 5316247340,f'Bot Is Not Admin In Channel ({i})')
   # bot.send_message(message.from_user.id,status)
        if status.status == 'left' or status.status == 'kicked':
            check = False
    if check == False:
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.row("🟢 Joined")
        user_id = message.chat.id
        bot.send_message(user_id,f"<b>❌ Mᴜsᴛ Jᴏɪɴ Aʟʟ Cʜᴀɴɴᴇʟs</b>",parse_mode="HTML")
        bot.send_photo(user_id,photo="https://t.me/Bots_Pay_Alert/880",caption=f"""<b>⛔ Mᴜꜱᴛ Jᴏɪɴ Oᴜʀ Aʟʟ ᴄʜᴀɴɴᴇʟs\n\n{ytchannel}</b>""", reply_markup=Channel_keyboard, parse_mode='HTML')
        bot.send_message(user_id,f"""<b>✅ Aꜰᴛᴇʀ  Jᴏɪɴɪɴɢ Aʟʟ Cʜᴀɴɴᴇʟs, Cʟɪᴄᴋ Oɴ '🟢 Jᴏɪɴᴇᴅ'</b>""", reply_markup=keyboard, parse_mode='HTML')
    else:
        user_id = get_data(f'{bot_id}-{message.from_user.id}-refer.json')
        handle_menu(message)
        bot_user = get_data(f'{bot_id}-{message.from_user.id}-bot_user')
        if bot_user == True:
        	return
        if user_id == "@None":
        	return
        elif user_id == None:
        	return
        add_balance(user_id,per_refer)
        balance = get_balance(user_id)
        bot.send_message(user_id,f"<b>💰 {per_refer} Pᴏɪɴᴛ Aᴅᴅᴇᴅ Tᴏ Yᴏᴜʀ Bᴀʟᴀɴᴄᴇ</b>",parse_mode='HTML')
        save_data(f'{bot_id}-{message.from_user.id}-bot_user',True)
        time.sleep(10)

def handle_menu(message):
    user_id = message.from_user.id
    welcome_message = get_data(f'{bot_id}-home_text.json')
    if str(welcome_message) == str(None):
    	welcome_message = "*🏡 Wᴇʟᴄᴏᴍᴇ Tᴏ Mᴀɪɴ Mᴇɴᴜ\n\n👉 Tʜᴇ Bᴏᴛ Is Pᴏᴡᴇʀᴇᴅ / Cᴏᴅᴇᴅ Bʏ @MrrrAdarsh 🤟*"
    options = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    options.row('💰 Bᴀʟᴀɴᴄᴇ', '👫 Rᴇꜰᴇʀʀᴀʟ')
    options.row('📤 Wɪᴛʜᴅʀᴀᴡ [ Cᴏᴅᴇ ]')
    options.row('🎁 Bᴏɴᴜs', '🆘 Sᴜᴘᴘᴏʀᴛ', '🌎 Sᴛᴀᴛɪsᴛɪᴄs')
    options.row('🛒 Pᴜʀᴄʜᴀsᴇ Bᴏᴛs / Cᴏᴅᴇs')
    bot.send_message(user_id, welcome_message, reply_markup=options, parse_mode='markdown')

@bot.message_handler(func=lambda message: message.text != '🟢 Joined')
def Bot_Off(message):
    msg = message.text
    if msg == '💰 Bᴀʟᴀɴᴄᴇ' or msg == '🛒 Pᴜʀᴄʜᴀsᴇ Bᴏᴛs / Cᴏᴅᴇs' or msg == '👫 Rᴇꜰᴇʀʀᴀʟ' or msg == '📤 Wɪᴛʜᴅʀᴀᴡ [ Cᴏᴅᴇ ]' or msg == '🎁 Bᴏɴᴜs' or msg == '🌎 Sᴛᴀᴛɪsᴛɪᴄs' or msg == '🆘 Sᴜᴘᴘᴏʀᴛ' or msg == "/set_home_text" or msg == '/broadcast' or msg == '/balance' or msg == '🛒 10Rs Rᴇᴇᴅᴇᴍ Cᴏᴅᴇ 😘' or msg =='/add_balance' or msg == '🔙 Bᴀᴄᴋ 🔙' or msg == '🛒 25Rs Rᴇᴇᴅᴇᴍ Cᴏᴅᴇ 😍':
        if bot_status == "Over":
            user_link = f'<a href="tg://user?id={message.from_user.id}">{message.from_user.first_name}</a>'
            bot.send_message(message.from_user.id,f'''<b>👋  Hᴇʟʟᴏ  {user_link}

⚠️ Bᴏᴛ Is Oᴠᴇʀ Nᴏᴡ. I Hᴏᴘᴇ Yᴏᴜ Lᴏᴏᴛᴇᴅ Oᴜʀ Bᴏᴛs ❌

❤️ Tʜᴀɴᴋs Fᴏʀ Usɪɴɢ Oᴜʀ Bᴏᴛ.
#BʏᴇFʀɪᴇɴᴅ #OᴠᴇʀNᴏᴡ #NᴇᴡSᴏᴏɴ</b>''', parse_mode='HTML')
        else:
            if msg == '💰 Bᴀʟᴀɴᴄᴇ':
                account(message)
            elif msg == "👫 Rᴇꜰᴇʀʀᴀʟ":
                invite(message)
            elif msg == "🗳️ Wallet":
                wallet(message)
            elif msg == '🆘 Sᴜᴘᴘᴏʀᴛ':
                sos(message)
            elif msg =="🛒 Pᴜʀᴄʜᴀsᴇ Bᴏᴛs / Cᴏᴅᴇs":
            	note(message)
            elif msg =='🌎 Sᴛᴀᴛɪsᴛɪᴄs':
                stats(message)
            elif msg == "/set_home_text":
            	set_home_text(message)
            elif msg == "🎁 Bᴏɴᴜs":
            	bonus(message)
            elif msg == '/broadcast':
            	handle_broadcast_command(message)
            elif msg == '/add_balance':
            	add_balance(message) 
            elif msg == '/balance':
            	handle_balance_command(message)   
            elif msg == '📤 Wɪᴛʜᴅʀᴀᴡ [ Cᴏᴅᴇ ]':
            	withdraw(message) 
            elif msg == '🛒 10Rs Rᴇᴇᴅᴇᴍ Cᴏᴅᴇ 😘':
            	withdraw_10(message)
            elif msg == '🛒 25Rs Rᴇᴇᴅᴇᴍ Cᴏᴅᴇ 😍':
            	withdraw_30(message)
            elif msg == '🔙 Bᴀᴄᴋ 🔙':
            	handle_menu(message)	
    else:
        if msg == "⛔ Cancel":
            handle_menu(message)
        else:
            bot.send_message(message.chat.id, '*❌ This Command Is Invalid , If You Think You Have Sent A Valid Command , Please Restart Bot Using /start*', parse_mode='markdown')

def account(message):
    balance = get_balance(message.from_user.id)
    user_link = f'<a href="tg://user?id={message.from_user.id}">{message.from_user.first_name}</a>'
    response_message = f"<b>🇮🇳 Usᴇʀ = {user_link}\n🧐 Usᴇʀ ɪᴅ:</b><code> {message.chat.id}</code><b>\n💰 Bᴀʟᴀɴᴄᴇ: {balance} Pᴏɪɴᴛs\n\n⏱ Tʜɪs Sᴛᴀᴛᴜs Rᴇᴘᴏʀᴛ Tᴀᴋᴇɴ Oɴ {formatted_date} Aᴛ {formatted_time}</b>"
    bot.send_message(message.chat.id, response_message, parse_mode='HTML')

def invite(message):
    inline_keyboard = types.InlineKeyboardMarkup()
    generate_button = types.InlineKeyboardButton(text="❤️ Sʜᴀʀᴇ Lɪɴᴋ ↗️", url=f"""https://telegram.me/share/url?url=👉 https://t.me/{bot.get_me().username}?start={message.chat.id} 👈\n&text=❤️%20Dᴏɴ'ᴛ%20Mɪss%20Tʜɪs%20Cʜᴀɴᴄᴇ%20Tᴏ%20Gʀᴀʙ%20Fʀᴇᴇ%20Rᴇᴇᴅᴇᴍ%20Cᴏᴅᴇs%20Jᴜsᴛ%20Bʏ%20Sʜᴀʀɪɴɢ%20Yᴏᴜʀ%20Rᴇғᴇʀʀᴀʟ%20Lɪɴᴋ%20Tᴏ%20Yᴏᴜʀ%20Fʀɪᴇɴᴅs%20Aɴᴅ%20Iɴᴠɪᴛɪɴɢ%20Tʜᴇᴍ%20Tᴏ%20Jᴏɪɴ%20Us""")
    inline_keyboard.add(generate_button)
    user_link = f'<a href="tg://user?id={message.from_user.id}">{message.from_user.first_name}</a>'
    invi_link = f'https://t.me/{bot.get_me().username}?start={message.chat.id}'
    bot.send_message(message.chat.id, f"""<b>🔰 Usᴇʀ = {user_link}\n\n🔥 Yᴏᴜʀ Lɪɴᴋ 👇👇👇👇👇\n{invi_link}\n\n🧬 Iɴᴠɪᴛᴇ Aɴᴅ Eᴀʀɴ {per_refer} Pᴏɪɴᴛs Pᴇʀ Rᴇꜰᴇʀʀᴀʟ</b>""", parse_mode='HTML', reply_markup=inline_keyboard)

def sos(message):
    if earn_text != None:
        bot.send_message(message.from_user.id,earn_text,parse_mode="HTML",reply_markup=Developer_keyboard)
        
def note(message):
    Note_keyboard = types.InlineKeyboardMarkup()
    Notice_button = types.InlineKeyboardButton(text="💖 Cʜᴀᴛ Wɪᴛʜ Mᴇ ↗️", url="https://t.me/MrAdarshG")
    Note_keyboard.add(Notice_button)
    user_link = f'<a href="tg://user?id={message.from_user.id}">{message.from_user.first_name}</a>'
    bot.send_photo(message.chat.id,photo="https://t.me/Bots_Pay_Alert/863",caption=f"""<b>👋 Hᴇʏ  {user_link}
➖➖➖➖➖➖➖➖➖➖➖➖➖
🛒 Oʜ !! Yᴏᴜ Nᴇᴇᴅ ᴀ Bᴏᴛ Fᴏʀ Yᴏᴜʀsᴇʟғ. Wᴇ Cᴀɴ Mᴀᴋᴇ ɪᴛ Fᴏʀ Yᴏᴜ.

👉 Wᴇ'ʀᴇ Pʀᴏʙᴀʙʟʏ Cʀᴇᴀᴛɪɴɢ Aʟʟ Kɪɴᴅs Oғ Bᴏᴛs. Jᴜsᴛ Cᴏᴍᴇ Aɴᴅ Tᴀʟᴋ Tᴏ Us.

🚀 Rᴇᴍᴇᴍʙᴇʀ:- Wᴇ Dᴏ Nᴏᴛ Cʀᴇᴀᴛᴇ Fʀᴇᴇ Bᴏᴛ Sᴏ Pᴀʏ Us Aɴᴅ Aᴠᴀɪʟ Oᴜʀ Sᴇʀᴠɪᴄᴇs.

👇Sᴛᴀʀᴛ Cʜᴀᴛᴛɪɴɢ Wɪᴛʜ Dᴇᴠᴇʟᴏᴘᴇʀ 👇</b>""", parse_mode='HTML',reply_markup=Note_keyboard)

def stats(message):
    user =  get_data(f"{bot_id}-user_id.json")
    order = get_data(f"{bot_id}-order.json")
    point = get_data(f"{bot_id}-point.json")
    if order == None:
    	order = 0
    if point == None:
    	point = 0
    if user == None:
    	user = 0
    else:
    	user = len(user)
    bot.send_photo(message.chat.id,photo="https://t.me/Bots_Pay_Alert/876",caption=f"""<b>📊 Bᴏᴛ Lɪᴠᴇ Sᴛᴀᴛᴜs Rᴇᴘᴏʀᴛ 📊

👥 Tᴏᴛᴀʟ Mᴇᴍʙᴇʀs: {user} Usᴇʀs

💸 Tᴏᴛᴀʟ Oʀᴅᴇʀs: {order} Oʀᴅᴇʀs

🛒 Oʀᴅᴇʀs Iɴ Pᴏɪɴᴛs: {point} Pᴏɪɴᴛs

🎭 Cʀᴇᴀᴛᴇᴅ Bʏ: @MrrrAdarsh</b>""", parse_mode='HTML')
def set_home_text(message):
	u = message.from_user.id
	if u !=  5316247340:
		return
	else:
		bot.send_message(u,f"*💡 Send New Home Text (Use MarkDown)*",parse_mode='markdown')
		bot.register_next_step_handler(message, save_home_text)	
def save_home_text(message):
	save_data(f'{bot_id}-home_text.json',message.text)
	bot.send_message(message.from_user.id,'<b>👍 Updated Home Text</b>',parse_mode='HTML')		
# Start the bot
def bonus(message):
    user_id = message.from_user.id
    bonus = get_data(f"{bot_id}-{user_id}-bonus.json")
    bonamount = float(1)  # Assuming bonamount is defined elsewhere in your code

    def conv(time):
        sec = time % (24 * 3600)
        hour = sec // 3600
        sec %= 3600
        mins = sec // 60
        sec %= 60
        return "%d:%02d:%02d" % (hour, mins, sec)

    cur_time = int((time.time()))

    if (bonus is None) or (cur_time - bonus > 24*60*60):
        save_data(f"{bot_id}-{user_id}-bonus.json", cur_time)
        add_balance(user_id, bonamount)  # Make sure to pass user_id and bonamount as parameters
        bot.send_message(user_id, f"*🎁 Cᴏɴɢʀᴀᴛs, Yᴏᴜ Rᴇᴄɪᴇᴠᴇᴅ {bonamount} Pᴏɪɴᴛ\n\n🔍 Cʜᴇᴄᴋ Bᴀᴄᴋ Aғᴛᴇʀ 24 Hᴏᴜʀs*", parse_mode='markdown')
    else:
        remaining_time = conv(bonus + 24*60*60 - cur_time)
        bot.send_message(user_id, f"*⛔ Yᴏᴜ Aʟʀᴇᴀᴅʏ Rᴇᴄᴇɪᴠᴇᴅ Bᴏɴᴜꜱ ɪɴ Lᴀꜱᴛ 24 Hᴏᴜʀꜱ\n\n🎁 Cᴏᴍᴇ Bᴀᴄᴋ Aꜰᴛᴇʀ: {remaining_time}*", parse_mode='markdown')
@bot.message_handler(commands=['broadcast'])
def handle_broadcast_command(message):
    if message.chat.id !=  5316247340:
        return
    else:
        msg = bot.send_message(message.chat.id, f"""<b>Pʟᴇᴀsᴇ Eɴᴛᴇʀ Tʜᴇ Mᴇssᴀɢᴇ Yᴏᴜ Wᴀɴᴛ Tᴏ Bʀᴏᴀᴅᴄᴀsᴛ:- 👇👇👇</b>""",parse_mode='HTML')
        bot.register_next_step_handler(msg, handle_broadcast_message)

def handle_broadcast_message(message):
    chat_id = message.chat.id
    broadcast_message = message.text

    # Get the list of users from user_list.json (assuming get_data is implemented correctly)
    user_list = get_data(f"{bot_id}-user_id.json")
    if user_list is None:
        bot.send_message(chat_id, "Error: User list not found.")
        return

    total_users = len(user_list)
    total_success = 0
    total_fail = 0

    # Broadcast the message to all users in the user list using copy_message
    for user_id in user_list:
        try:
            bot.copy_message(chat_id=user_id, from_chat_id=chat_id, message_id=message.message_id)
            total_success += 1
        except Exception as e:
            total_fail += 1

    # Emoji Unicode for visual appeal
    success_emoji = u'\U0001F60E'  # Smiling Face Emoji
    fail_emoji = u'\U0001F622'  # Crying Face Emoji

    # Compose the message with total counts and emojis
    response_message = f"Bʀᴏᴀᴅᴄᴀsᴛ Sᴜᴍᴍᴀʀʏ 👇👇👇\n\n"
    response_message += f"Tᴏᴛᴀʟ Usᴇʀs: {total_users}\n"
    response_message += f"Tᴏᴛᴀʟ Sᴜᴄᴄᴇss: {total_success} {success_emoji}\n"
    response_message += f"Tᴏᴛᴀʟ Fᴀɪʟᴇᴅ: {total_fail} {fail_emoji}\n"

    bot.send_message(chat_id, response_message)
    
def withdraw(message):
	Keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
	Keyboard.row('🛒 10Rs Rᴇᴇᴅᴇᴍ Cᴏᴅᴇ 😘')
	Keyboard.row('🛒 25Rs Rᴇᴇᴅᴇᴍ Cᴏᴅᴇ 😍')
	Keyboard.row('🔙 Bᴀᴄᴋ 🔙')
	u = message.from_user.id
	bot.send_message(u,f"""<b>🤟 Sᴇʟᴇᴄᴛ Aɴʏ Oɴᴇ Fʀᴏᴍ Bᴇʟᴏᴡ Oᴘᴛɪᴏɴs Tᴏ Pʀᴏᴄᴇᴇᴅ 🔥

🛒 10Rs Cᴏᴅᴇ 😘 = 15 Pᴏɪɴᴛs 
🛒 25Rs Cᴏᴅᴇ 😍 = 30 Pᴏɪɴᴛs</b>""",parse_mode="HTML",reply_markup=Keyboard)
def withdraw_10(message):
	u = message.from_user.id
	balance = get_balance(u)
	if balance < 15:
		bot.send_message(u,f"*❌ Yᴏᴜ Hᴀᴠᴇ Tᴏ Oᴡɴ Aᴛ Lᴇᴀꜱᴛ 15 Pᴏɪɴᴛꜱ*",parse_mode='markdown')
		return
	bot.send_message(u,f"*🔰 Sᴇɴᴅ Uꜱᴇʀɴᴀᴍᴇ Wʜᴇʀᴇ Yᴏᴜ Wᴀɴᴛ Tᴏ Gᴇᴛ Rᴇᴇᴅᴇᴍ Cᴏᴅᴇ (Sᴇɴᴅ Uꜱᴇʀɴᴀᴍᴇ Oɴʟʏ )*",parse_mode='markdown',reply_markup=types.ReplyKeyboardRemove())
	bot.register_next_step_handler(message,do_withdraw_10)
def do_withdraw_10(message):	
	msg = message.text
	u = message.from_user.id
	Keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
	Keyboard.row('✅ Aᴘᴘʀᴏᴠᴇ')
	Keyboard.row('❌ Rᴇᴊᴇᴄᴛ')
	bot.send_message(u,f"""*🛒 Yᴏᴜʀ Oʀᴅᴇʀ Dᴇᴛᴀɪʟꜱ 🛒

❤️ Yᴏᴜʀ Uꜱᴇʀɴᴀᴍᴇ = {msg}

🎉 Pᴀᴄᴋ = 🛒 10Rs Rᴇᴇᴅᴇᴍ Cᴏᴅᴇ

💸 Pʀɪᴄᴇs = 15 Pᴏɪɴᴛs

📑 Nᴏᴛᴇ = Wᴇ Wɪʟʟ Tʀʏ Tᴏ Cᴏᴍᴘʟᴇᴛᴇ Yᴏᴜʀ Oʀᴅᴇʀ Aꜱ Aᴏᴏɴ Aꜱ Pᴏꜱꜱɪʙʟᴇ 😍*""",parse_mode='Markdown',reply_markup=Keyboard)
	bot.register_next_step_handler(message,done_withdraw_10)	
	save_data(f'{bot_id}-{u}-wallet.json',message.text)
def done_withdraw_10(message):
	if message.text == "✅ Aᴘᴘʀᴏᴠᴇ":
		pass
	else:
		handle_menu(message)
		return
	u = message.from_user.id
	order = get_data(f"{bot_id}-order.json")
	point = get_data(f"{bot_id}-point.json")
	if order == None:
	    order = 0
	if point == None:
	    point = 0
	order = int(order)+1
	point = int(point)+15
	save_data(f"{bot_id}-point.json",point)
	save_data(f"{bot_id}-order.json",order)
	add_balance(u,-16)
	user_refer = 15
	wallet = get_data(f'{bot_id}-{u}-wallet.json')
	markup = types.InlineKeyboardMarkup()
	url_button = types.InlineKeyboardButton(text="🛒 Pᴜʀᴄʜᴀsᴇ Nᴏᴡ ↗️",     url=f"https://t.me/{bot.get_me().username}")
	markup.add(url_button)
	Payout = types.InlineKeyboardMarkup()
	Purl_button = types.InlineKeyboardButton(text="🕊 Mᴏʀᴇ Dᴇᴛᴀɪʟs 🔥",     url=f"https://t.me/{payout}")
	Payout.add(Purl_button)
	bot.send_message(f'@{payout}',f"""<b>📦 Nᴇᴡ Oʀᴅᴇʀ Pʟᴀᴄᴇᴅ Bʏ 👍👍👍
{message.from_user.first_name}

◼️ Sᴛᴀᴛᴜꜱ = Pʀᴏᴄᴇꜱꜱɪɴɢ....

🥡 Pᴀᴄᴋ = 🛒 10Rs Rᴇᴇᴅᴇᴍ Cᴏᴅᴇ

💸 Aᴍᴏᴜɴᴛ = 15 Pᴏɪɴᴛꜱ 

😍 Uꜱᴇʀ ɪᴅ = {u}

❤️ Uꜱᴇʀɴᴀᴍᴇ = {wallet}  [ Wᴀʟʟᴇᴛ ]

💝 Bᴏᴛ Pᴏᴡᴇʀᴇᴅ Bʏ @MʀʀʀAᴅᴀʀsʜ👈</b>""",parse_mode="HTML",reply_markup=markup)
	bot.send_message(u,f"""<b>🛒 Yᴏᴜʀ Oʀᴅᴇʀ Dᴇᴛᴀɪʟꜱ 🛒

❤️ Yᴏᴜʀ Uꜱᴇʀɴᴀᴍᴇ = {wallet}
🎉 Pᴀᴄᴋ = 🛒 10Rs Rᴇᴇᴅᴇᴍ Cᴏᴅᴇ
💸 Pʀɪᴄᴇ = 15 Pᴏɪɴᴛs

📑 Nᴏᴛᴇ =  Wᴇ Hᴀᴠᴇ Tᴏᴏ Mᴜᴄʜ Oʀᴅᴇʀꜱ Sᴏ Wᴇ Cᴀɴᴛ Cᴏᴍᴘʟᴇᴛᴇ Yᴏᴜʀ Qᴜɪᴄᴋʟʏ 😊</b>""",parse_mode='HTmL',reply_markup=Payout)
	handle_menu(message)
def withdraw_30(message):
	u = message.from_user.id
	balance = get_balance(u)
	if balance < 30:
		bot.send_message(u,f"*❌ Yᴏᴜ Hᴀᴠᴇ Tᴏ Oᴡɴ Aᴛ Lᴇᴀꜱᴛ 30 Pᴏɪɴᴛꜱ*",parse_mode='markdown')
		return
	bot.send_message(u,f"*🔰 Sᴇɴᴅ Uꜱᴇʀɴᴀᴍᴇ Wʜᴇʀᴇ Yᴏᴜ Wᴀɴᴛ Tᴏ Gᴇᴛ Rᴇᴇᴅᴇᴍ Cᴏᴅᴇ (Sᴇɴᴅ Uꜱᴇʀɴᴀᴍᴇ Oɴʟʏ )*",parse_mode='markdown',reply_markup=types.ReplyKeyboardRemove())
	bot.register_next_step_handler(message,do_withdraw_30)
def do_withdraw_30(message):	
	msg = message.text
	u = message.from_user.id
	Keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
	Keyboard.row('✅ Aᴘᴘʀᴏᴠᴇ')
	Keyboard.row('❌ Rᴇᴊᴇᴄᴛ')
	bot.send_message(u,f"""*🛒 Yᴏᴜʀ Oʀᴅᴇʀ Dᴇᴛᴀɪʟꜱ 🛒

❤️ Yᴏᴜʀ Uꜱᴇʀɴᴀᴍᴇ = {msg}

🎉 Pᴀᴄᴋ = 🛒 25Rs Rᴇᴇᴅᴇᴍ Cᴏᴅᴇ

💸 Pʀɪᴄᴇs = 30 Pᴏɪɴᴛs

📑 Nᴏᴛᴇ = Wᴇ Wɪʟʟ Tʀʏ Tᴏ Cᴏᴍᴘʟᴇᴛᴇ Yᴏᴜʀ Oʀᴅᴇʀ Aꜱ Aᴏᴏɴ Aꜱ Pᴏꜱꜱɪʙʟᴇ 😍*""",parse_mode='Markdown',reply_markup=Keyboard)
	bot.register_next_step_handler(message,done_withdraw_30)	
	save_data(f'{bot_id}-{u}-wallet.json',message.text)
def done_withdraw_30(message):
	if message.text == "✅ Aᴘᴘʀᴏᴠᴇ":
		pass
	else:
		handle_menu(message)
		return
	u = message.from_user.id
	order = get_data(f"{bot_id}-order.json")
	point = get_data(f"{bot_id}-point.json")
	if order == None:
	    order = 0
	if point == None:
	    point = 0
	order = int(order)+1
	point = int(point)+30
	save_data(f"{bot_id}-point.json",point)
	save_data(f"{bot_id}-order.json",order)
	add_balance(u,-30)
	user_refer = 15
	wallet = get_data(f'{bot_id}-{u}-wallet.json')
	markup = types.InlineKeyboardMarkup()
	url_button = types.InlineKeyboardButton(text="🛒 Pᴜʀᴄʜᴀsᴇ Nᴏᴡ ↗️",      url=f"https://t.me/{bot.get_me().username}")
	markup.add(url_button)
	Payout = types.InlineKeyboardMarkup()
	Purl_button = types.InlineKeyboardButton(text="🕊 Mᴏʀᴇ Dᴇᴛᴀɪʟs 🔥",     url=f"https://t.me/{payout}")
	Payout.add(Purl_button)
	bot.send_message(f'@{payout}',f"""<b>📦 Nᴇᴡ Oʀᴅᴇʀ Pʟᴀᴄᴇᴅ Bʏ 👍👍👍
{message.from_user.first_name}

◼️ Sᴛᴀᴛᴜꜱ = Pʀᴏᴄᴇꜱꜱɪɴɢ....

🥡 Pᴀᴄᴋ = 🛒 25Rs Rᴇᴇᴅᴇᴍ Cᴏᴅᴇ

💸 Aᴍᴏᴜɴᴛ = 30 Pᴏɪɴᴛs

😍 Uꜱᴇʀ ɪᴅ = {u}

❤️ Uꜱᴇʀɴᴀᴍᴇ = {wallet}  [ Wᴀʟʟᴇᴛ ]

💝 Bᴏᴛ Pᴏᴡᴇʀᴇᴅ Bʏ @MʀʀʀAᴅᴀʀsʜ👈</b>""",parse_mode="HTML",reply_markup=markup)
	bot.send_message(u,f"""<b>🛒 Yᴏᴜʀ Oʀᴅᴇʀ Dᴇᴛᴀɪʟꜱ 🛒

❤️ Yᴏᴜʀ Uꜱᴇʀɴᴀᴍᴇ = {wallet}
🎉 Pᴀᴄᴋ = 🛒 25Rs Rᴇᴇᴅᴇᴍ Cᴏᴅᴇ
💸 Pʀɪᴄᴇ = 30 Pᴏɪɴᴛs

📑 Nᴏᴛᴇ =  Wᴇ Hᴀᴠᴇ Tᴏᴏ Mᴜᴄʜ Oʀᴅᴇʀꜱ Sᴏ Wᴇ Cᴀɴᴛ Cᴏᴍᴘʟᴇᴛᴇ Yᴏᴜʀ Qᴜɪᴄᴋʟʏ 😊</b>""",parse_mode='HTmL',reply_markup=Payout)
	handle_menu(message)
bot.infinity_polling()