import telebot
import bot_py_lib

# Temperture inside the following file
tempr_file = '/home/projects/first_tbot/rasp_core_tempr'

# Make list of any possible commands
buttons = ['/start', 'w', 'get rasp core tempr', 'weather']

# Get bot chat id
with open('/root/tbot_id', 'r') as f:
    bot_id = f.readline().strip()

# Use bot chat id
bot = telebot.TeleBot(bot_id)

# Make individual keyboard with our commands
keyboard1 = telebot.types.ReplyKeyboardMarkup()
keyboard1.row(*buttons)

# Bot starts with command 'start', unexpectedly, isnt it?
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Hello', reply_markup=keyboard1)
    bot_py_lib.print_test(message)

# Bot executes commands
@bot.message_handler(content_types=['text'])
def sendText(message):
    if message.text == buttons[0]:
        bot.send_message(message.chat.id, 'Hello', reply_markup=keyboard1)
    elif message.text == buttons[1]:
        res = bot_py_lib.add_whois()
        bot.send_message(message.chat.id, res, parse_mode='Markdown', disable_web_page_preview=True)
    elif message.text == buttons[2]:
        try:
            with open(tempr_file, 'r') as f:
                res = f.readline()
            bot.send_message(message.chat.id, res)
        except:
            bot.send_message(message.chat.id, 'Нетути')
    else:
        bot.send_message(message.chat.id, 'А это фих знает шоb')

bot.polling()
