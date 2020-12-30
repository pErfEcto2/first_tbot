import telebot
import os
import subprocess
import re

with open('/root/tbot_id', 'r') as f:
    bot_id = f.readline().strip()

bot = telebot.TeleBot(bot_id)

buttons = ['1', 'w', 'get rasp core tempr']

keyboard1 = telebot.types.ReplyKeyboardMarkup(True)
keyboard1.row(*buttons)

def add_whois(t):
    t = t.decode('utf-8')
    l_str = t.split("\n")
    l1_line = []
    res_ip = []
    for line in l_str:
        ip = re.match(r"(.*\s)(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})(.*)", line)
        if ip:
            link = 'https://www.reg.ru/whois/?dname=' + ip.group(2)
            l2_line = line.split(" ")
            l1_line += l2_line[0:4]
            l1_line.append(link)
            l1_line += l2_line[5:-1]
            res_ip.append(' '.join(l1_line))
    return '\n'.join(res_ip)

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет', reply_markup=keyboard1) 

@bot.message_handler(content_types=['text'])
def sendText(message):
    if message.text == buttons[0]:
        bot.send_message(message.chat.id, 'Это единишка')
    elif message.text == buttons[1]:
        res = subprocess.run(['w'], stderr=subprocess.STDOUT, stdout=subprocess.PIPE)
        res = add_whois(res.stdout)
        bot.send_message(message.chat.id, res)
    elif message.text == buttons[2]:
        with open('/home/rasp_core_temp', 'r') as f:
            res = f.readline()
        bot.send_message(message.chat.id, res)
    else:
        bot.send_message(message.chat.id, 'А это фих знает шо')

bot.polling()