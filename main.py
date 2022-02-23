import config
import telebot
import requests
from bs4 import BeautifulSoup as bs
from telebot import types

bot = telebot.TeleBot(config.token)

r = requests.get('https://sinoptik.ua/погода-москва')
html = bs(r.content,'html.parser')

@bot.message_handler(commands=['weather'])
def findW(message):
    for i in range(7):
        for el in html.select('#content'):
            date = el.select('.main .date')[i].text
            month = el.select('.month')[i].text
            daylink = el.select('.day-link')[i].text
            t_min = el.select('.temperature .min')[i].text
            t_max = el.select('.temperature .max')[i].text
            description = el.select('.wDescription .description')[0].text
            bot.send_message(message.chat.id,date + month + '\n' + daylink +'\n' + t_max + t_min + '\n')


@bot.message_handler(commands=['today'])
def findOne(message):
    for el in html.select('#content'):
        date = el.select('.main .date')[0].text
        month = el.select('.month')[0].text
        daylink = el.select('.day-link')[0].text
        t_min = el.select('.temperature .min')[0].text
        t_max = el.select('.temperature .max')[0].text
        description = el.select('.wDescription .description')[0].text
        print(r)
        bot.send_message(message.chat.id, date + month + '\n' + daylink + '\n' + t_max + t_min + '\n' + description)




@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, 'Привет. Воспользуйся командами или введи команду /help')






bot.polling(none_stop=True)


