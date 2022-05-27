from pathlib import Path
first_round = {
    1: {"caption":"1 Раунд «Найди общее». В этом раунде тебе предстоит найти что-то общее, связывающее предметы на картинках.",'path': f"{Path(__file__).parent.absolute()}\\media\\1_1.png", "variant": ["дерево", "игра", "соревнование", "обучение"], 'right': "игра"},
    2: {"caption":"1 Раунд «Найди общее». В этом раунде тебе предстоит найти что-то общее, связывающее предметы на картинках.",'path': f"{Path(__file__).parent.absolute()}\\media\\1_2.png", "variant": ["бой", "фильм", "коса", "экшн"], 'right': "коса"},
    3: {"caption":"1 Раунд «Найди общее». В этом раунде тебе предстоит найти что-то общее, связывающее предметы на картинках.",'path': f"{Path(__file__).parent.absolute()}\\media\\1_3.png", "variant": ["утро", "овсянка", "деревня", "пиво"], 'right': "овсянка"},
    4: {"caption":"1 Раунд «Найди общее». В этом раунде тебе предстоит найти что-то общее, связывающее предметы на картинках.",'path': f"{Path(__file__).parent.absolute()}\\media\\1_4.png", "variant": ["стрела", "предательство", "боль", "пельмени"], 'right': "стрела"},
    5: {"caption":"1 Раунд «Найди общее». В этом раунде тебе предстоит найти что-то общее, связывающее предметы на картинках.",'path': f"{Path(__file__).parent.absolute()}\\media\\1_5.png", "variant": ["дизайн", "архитектура", "хобби", "камера"], 'right': "камера"},
    6: {"caption":"1 Раунд «Найди общее». В этом раунде тебе предстоит найти что-то общее, связывающее предметы на картинках.",'path': f"{Path(__file__).parent.absolute()}\\media\\1_6.png", "variant": ["традиция", "страны", "свадьба", "костюм"], 'right': "традиция"},
    7: {"caption":"1 Раунд «Найди общее». В этом раунде тебе предстоит найти что-то общее, связывающее предметы на картинках.",'path': f"{Path(__file__).parent.absolute()}\\media\\1_7.png", "variant": ["счёт", "загадка", "вложение", "ответственность"], 'right': "счёт"},
    8: {"caption":"1 Раунд «Найди общее». В этом раунде тебе предстоит найти что-то общее, связывающее предметы на картинках.",'path': f"{Path(__file__).parent.absolute()}\\media\\1_8.png", "variant": ["клип", "традиция", "кровь", "игла"], 'right': "игла"},
    9: {"caption":"1 Раунд «Найди общее». В этом раунде тебе предстоит найти что-то общее, связывающее предметы на картинках.",'path': f"{Path(__file__).parent.absolute()}\\media\\1_9.png", "variant": ["точки", "рыба", "бесконечность", "смысл"], 'right': "рыба"},
    10: {"caption":"1 Раунд «Найди общее». В этом раунде тебе предстоит найти что-то общее, связывающее предметы на картинках.",'path': f"{Path(__file__).parent.absolute()}\\media\\1_10.png", "variant": ["добыча", "плеть", "природа", "шеф повар"], 'right': "плеть"}}

second_round = {
    1: {"caption":"2 Раунд «Чего-то не хватает». На фотографии отсутствует один предмет, твоя задача понять, чего не хватает",'path': f"{Path(__file__).parent.absolute()}\\media\\2_1.png", "variant": ["горб", "пирамида", "солнце", "кактусы"], 'right': "горб"},
    2: {"caption":"2 Раунд «Чего-то не хватает». На фотографии отсутствует один предмет, твоя задача понять, чего не хватает",'path': f"{Path(__file__).parent.absolute()}\\media\\2_2.png", "variant": ["крабик", "следы", "тапки", "шезлонг"], 'right': "следы"},
    3: {"caption":"2 Раунд «Чего-то не хватает». На фотографии отсутствует один предмет, твоя задача понять, чего не хватает",'path': f"{Path(__file__).parent.absolute()}\\media\\2_3.png", "variant": ["верблюд", "туристы", "пирамида", "сфинкс"], 'right': "сфинкс"},
    4: {"caption":"2 Раунд «Чего-то не хватает». На фотографии отсутствует один предмет, твоя задача понять, чего не хватает",'path': f"{Path(__file__).parent.absolute()}\\media\\2_4.png", "variant": ["микрофон", "леденец", "слез", "родителей"], 'right': "микрофон"},
    5: {"caption":"2 Раунд «Чего-то не хватает». На фотографии отсутствует один предмет, твоя задача понять, чего не хватает",'path': f"{Path(__file__).parent.absolute()}\\media\\2_5.png", "variant": ["башня", "колизей", "статуя свободы", "туристы"], 'right': "башня"},
    6: {"caption":"2 Раунд «Чего-то не хватает». На фотографии отсутствует один предмет, твоя задача понять, чего не хватает",'path': f"{Path(__file__).parent.absolute()}\\media\\2_6.png", "variant": ["звезда", "дед мороз", "снеговик", "подарок"], 'right': "звезда"},
    7: {"caption":"2 Раунд «Чего-то не хватает». На фотографии отсутствует один предмет, твоя задача понять, чего не хватает",'path': f"{Path(__file__).parent.absolute()}\\media\\2_7.png", "variant": ["земля", "юпитер", "марс", "меркурий"], 'right': "марс"}}

third_round = {
    1: {"caption":"3 Раунд «Из песни слов не выкинешь».  Твоя задача подобрать правильное слово или выражение в песне.\n\nФотографирую… словно пару лет назад","variant": ["конспект", "закат", "тебя", "пейзаж"], 'right': "закат"},
    2: {"caption":"3 Раунд «Из песни слов не выкинешь».  Твоя задача подобрать правильное слово или выражение в песне.\n\nМне нравится, что вы…","variant": ["уступили место", "вкусно готовите", "крысивый", "больны не мной"], 'right': "больны не мной"},
    3: {"caption":"3 Раунд «Из песни слов не выкинешь».  Твоя задача подобрать правильное слово или выражение в песне.\n\nДля остальных я …","variant": ["плохой", "герой", "вне зоны доступа", "занят"], 'right': "занят"},
    4: {"caption":"3 Раунд «Из песни слов не выкинешь».  Твоя задача подобрать правильное слово или выражение в песне.\n\nУ любви моей … не считано","variant": ["дней", "девушек", "денег", "здоровья"], 'right': "дней"},
    5: {"caption":"3 Раунд «Из песни слов не выкинешь».  Твоя задача подобрать правильное слово или выражение в песне.\n\n… опустилась как облако ","variant": ["белая ночь", "любовь", "беда", "глупая случайность"], 'right': "белая ночь"},
    6: {"caption":"3 Раунд «Из песни слов не выкинешь».  Твоя задача подобрать правильное слово или выражение в песне.\n\nВеселятся твои подружки...всех","variant": ["разбудили", "накормили", "повеселили", "утомили"], 'right': "разбудили"},
    7: {"caption":"3 Раунд «Из песни слов не выкинешь».  Твоя задача подобрать правильное слово или выражение в песне.\n\nЕщё один раз, здесь только я и...","variant": ["ты", "еда", "рюмка водки", "деньги"], 'right': "ты"}}

fourth_round = {
    1: {"caption":"Раунд «Цитаты великих». Изречения великих нужно знать, поэтому тебе нужно подумать, какое слово пропущено в их изречениях.\n\nФранцузский философ Монтескье сказал - «Ни что так не содействует женитьбе, как возможность…","variant": ["возможность", "разбогатеть", "завести детей", "развода"], 'right': "развода"},
    2: {"caption":"Раунд «Цитаты великих». Изречения великих нужно знать, поэтому тебе нужно подумать, какое слово пропущено в их изречениях.\n\nМарк Твен - «Не многие из нас могут вынести счастье...","variant": ["ближнего", "врага", "незнакомца", "звезды"], 'right': "ближнего"},
    3: {"caption":"Раунд «Цитаты великих». Изречения великих нужно знать, поэтому тебе нужно подумать, какое слово пропущено в их изречениях.\n\nФаина Раневская - «Всё приятное в этом мире, либо вредно, либо аморально, либо…","variant": ["ведёт к распаду", "ожирению", "бедности", "несчастью"], 'right': "ожирению"},
    4: {"caption":"Раунд «Цитаты великих». Изречения великих нужно знать, поэтому тебе нужно подумать, какое слово пропущено в их изречениях.\n\nМаргарет Тэтчер сказала - «Брать у неё интервью всё равно что беседовать с…","variant": ["с самом собой", "с другом", "с мамой", "с автоответчиком"], 'right': "с автоответчиком"},
    5: {"caption":"Раунд «Цитаты великих». Изречения великих нужно знать, поэтому тебе нужно подумать, какое слово пропущено в их изречениях.\n\nвуди Аллен - американский кинорежиссёр, актер - как то сказал - «У смерти есть и хорошая сторона, это одно из немногих дел"
        "которые легко делать...","variant": ["на работе", "с закрытыми глазами", "безответственно", "лежа"], 'right': "лежа"},
    6: {"caption":"Раунд «Цитаты великих». Изречения великих нужно знать, поэтому тебе нужно подумать, какое слово пропущено в их изречениях.\n\nКОГДА ТО ПРЕМЬЕР МИНИСТР Англии Бенджамин Дизраэли сказал: «Есть три разновидности лжи - ложь, гнусная ложь и...","variant": ["правда", "стаситика", "клевета", "безразличие"], 'right': "стаситика"},
    7: {"caption":"Раунд «Цитаты великих». Изречения великих нужно знать, поэтому тебе нужно подумать, какое слово пропущено в их изречениях.\n\nТорнтон Уайлдер - американский прозаик и драматург, однажды сказал - «Мужчина может править миром и стяжать славу своей"
        "мудростью, но в глазах жены он останется-...","variant": ["идиотом", "героем", "мальчиком", "тигром","безмозглым идиотом"], 'right': "безмозглым идиотом"}}
cap = "Привет! В этом боте ты сможешь сыграть в игру по мотивам популярного шоу «Где логика?», состоящую из четырёх раундов.\n*Готовы начать?*"

