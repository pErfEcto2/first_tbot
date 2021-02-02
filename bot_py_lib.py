# Im using this lib for my telegram bot
import re
import telebot
import os
import subprocess
import time
import telebot

with open('/root/tbot_id', 'r') as f:
    bot_id = f.readline().strip()

bot = telebot.TeleBot(bot_id)

# Execute bash command "w"
def do_w():
    res = subprocess.run(['w'], stderr=subprocess.STDOUT, stdout=subprocess.PIPE)
    return res.stdout.decode('utf-8')

# Find ip addr after function "do_w" and make hyperlink to whois
def add_whois():
    res_w = do_w()
    list_str = res_w.split("\n")
    result = ''
    for line in list_str:
        re_res = re.match(r"(.*\s)(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})(\s.*)", line)
        if not re_res:
            result += line + '\n'
        else:
            ip = re_res.group(2)
            link = f'[{ip}](https://www.reg.ru/whois/?dname={ip})'
            list2_line = line.split()
            first_part = " ".join(list2_line[:2])
            last_part = " ".join(list2_line[3:])
            result += f"{first_part} {link} {last_part}"
    return result

# Testing feature
def print_test(message):
    for _ in range(3):
        bot.send_message(message.chat.id, "Test")
        time.sleep(2)