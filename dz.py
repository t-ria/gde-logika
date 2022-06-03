
def dz1(bot, chat_id):
    dz1_ResponseHandler = lambda message: bot.send_message(chat_id, f'Привет, {message.text}!')
    my_input(bot, chat_id, 'Введите ваше имя:', dz1_ResponseHandler)

#-------------------------------------------------------------------------------------------------

def dz2(bot, chat_id):
    def dz2_ResponseHandler(bot, chat_id, age_int):
        bot.send_message(chat_id, text=f"Вам {age_int} лет!")

    my_inputInt(bot, chat_id, "Сколько вам лет?", dz2_ResponseHandler)

#--------------------------------------------------------------------------------------------------

def dz3(bot, chat_id):
    dz3_ResponseHandler = lambda message: bot.send_message(chat_id, f"{message.text*5}")
    my_input(bot, chat_id, 'Введите ваше имя:', dz3_ResponseHandler)

#--------------------------------------------------------------------------------------------------

def dz45(bot, chat_id):
    def dz45_ResponseHandler(bot, chat_id, age):
        if 0 < age < 7:
            bot.send_message(chat_id, "Почему ты не в садике")
        if 8 < age < 18:
            bot.send_message(chat_id, "Иди делай уроки <3")
        if age > 19:
            bot.send_message(chat_id, "Какого это жить в ваши " + str(age) + "?")

    my_inputInt(bot, chat_id, "Введите возраст.", dz45_ResponseHandler)

#--------------------------------------------------------------------------------------------------

def dz6(bot, chat_id):
    dz6_ResponseHandler = lambda message: bot.send_message(chat_id, f"Привет, {message.text}! Смотри \n"
                                                                    f"{str(message.text[1:len(message.text) - 1:])}\n"
                                                                    f"{str(message.text[::-1])}\n"
                                                                    f"{str(message.text[-3::])}\n"
                                                                    f"{str(message.text[:5:])}\n")
    my_input(bot, chat_id, 'Введите ваше имя:', dz6_ResponseHandler)

#--------------------------------------------------------------------------------------------------




















#дописать
def my_input(bot, chat_id, txt, ResponseHandler):
    message = bot.send_message(chat_id, text=txt)
    bot.register_next_step_handler(message, ResponseHandler)

def my_inputInt(bot, chat_id, txt, ResponseHandler):

    message = bot.send_message(chat_id, text=txt)
    bot.register_next_step_handler(message, my_inputInt_SecondPart, botQuestion=bot, txtQuestion=txt, ResponseHandler=ResponseHandler)

def my_inputInt_SecondPart(message, botQuestion, txtQuestion, ResponseHandler):
    chat_id = message.chat.id
    try:
        var_int = int(message.text)
        ResponseHandler(botQuestion, chat_id, var_int)
    except ValueError:
        botQuestion.send_message(chat_id,
                         text="Можно вводить ТОЛЬКО целое число в десятичной системе исчисления (символами от 0 до 9)!\nПопробуйте еще раз...")
        my_inputInt(botQuestion, chat_id, txtQuestion, ResponseHandler)

def my_inputStr(bot, chat_id, txt, ResponseHandler):
    message = bot.send_message(chat_id, text=txt)
    bot.register_next_step_handler(message, my_inputStr_SecondPart, botQuestion=bot, txtQuestion=txt,
                                   ResponseHandler=ResponseHandler)

def my_inputStr_SecondPart(message, botQuestion, txtQuestion, ResponseHandler):
    chat_id = message.chat.id

    var_str = str(message.text)
    ResponseHandler(botQuestion, chat_id, var_str)