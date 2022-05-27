import telebot
from telebot import types
from data import *
import io
import PIL.Image as Image
import random
import time

TOKEN = "5129343704:AAEQ0O6FhQ_tno-PJzgaLe4cDy0vZHGWa00"

bot = telebot.TeleBot(TOKEN)
users = {}

def generate_menu(button_list):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard = True)
    [keyboard.add(button) for button in button_list]
    return keyboard

def img_caption(message,round,number):
    rand_img = random.randint(1,number)
    with Image.open(round[rand_img]['path']) as img:
        b = io.BytesIO()
        img.save(b, 'png')
        img_bytes = b.getvalue()
    bot.send_photo(message.from_user.id, caption=round[rand_img]['caption'], photo=img_bytes, reply_markup=generate_menu(round[rand_img]['variant']))
    users[message.from_user.id]['random'] = rand_img

def next_round(message,round,number):
    rand = random.randint(1,number)
    bot.send_message(message.from_user.id, round[rand]['caption'], reply_markup=generate_menu(round[rand]['variant']))
    users[message.from_user.id]['random'] = rand

@bot.message_handler(commands=['start'])
def start_menu(message):
    button_list = ["Начать!"]

    bot.send_photo(message.from_user.id,"https://i.ytimg.com/vi/f7h4CphLOqA/maxresdefault.jpg",cap, reply_markup=generate_menu(button_list),parse_mode='Markdown')
    bot.delete_message(message.chat.id, message.message_id)


@bot.message_handler(content_types=['text'])
def initilize(message):
    if message.text == "Начать!":
        users.update({message.from_user.id: {'random': 10, 'count': 0, 'number': first_round}})
        first(message)

def answer(message):
    print(users)
    rand_img = users[message.from_user.id]['random']
    number = users[message.from_user.id]['number']
    users[message.from_user.id]['count']+=(1 if number[rand_img]['right'] == message.text else 0)
    result = "CAACAgIAAxkBAAEE0opijwqvUm6wKJl2vhrkUfV6FLBrhQAC-RUAAvncqUufzmIMG6ogyCQE" if number[rand_img]['right'] == message.text else "CAACAgIAAxkBAAEE0oxijwstKbixeyBy3Bqljz0Ec2BEEgACDwwAAuKOOUotFzfMTUK3UCQE"
    bot.delete_message(message.chat.id, message.message_id)
    bot.send_sticker(message.chat.id, result)

def first(message):

    img_caption(message,first_round,10)

    bot.register_next_step_handler(message,second)

def second(message):
    answer(message)
    users[message.from_user.id]['number']=second_round
    img_caption(message,second_round,7)
    bot.register_next_step_handler(message, third)

def third(message):
    answer(message)
    users[message.from_user.id]['number'] = third_round
    next_round(message,third_round,7)
    bot.register_next_step_handler(message, fourth)

def fourth(message):

    answer(message)
    users[message.from_user.id]['number'] = fourth_round
    next_round(message,fourth_round,7)
    bot.register_next_step_handler(message, end)

def end(message):
    answer(message)
    bot.send_sticker(message.from_user.id, "CAACAgIAAxkBAAEE0o5ijwv_fKvjGUohubXMPIp5x-pPAgACswsAAipQUUoso7YJ7GnT1iQE")

    bot.send_message(message.from_user.id,f'Поздравляю! Вы прошли викторину!\n\nВы набрали {users[message.from_user.id]["count"]} очков\n\nХотите сыграть еще раз?', reply_markup=generate_menu(["Начать!"]))
bot.infinity_polling()
