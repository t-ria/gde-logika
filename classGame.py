from telebot import types
import random
import PIL.Image as Image
import io
import telebot

import config
from config import users

bot = telebot.TeleBot(config.TOKEN)


class Game:
    def generate_menu(button_list):
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        [keyboard.add(button) for button in button_list]
        return keyboard

    def img_caption(message, round, number):
        rand_img = random.randint(1, number)
        with Image.open(round[rand_img]['path']) as img:
            b = io.BytesIO()
            img.save(b, 'png')
            img_bytes = b.getvalue()
        bot.send_photo(message.from_user.id, caption=round[rand_img]['caption'], photo=img_bytes,
                       reply_markup=Game.generate_menu(round[rand_img]['variant']))
        users[message.from_user.id]['random'] = rand_img
