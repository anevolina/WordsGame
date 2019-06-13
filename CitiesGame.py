import random

citiesF = open("cities.txt", "r", encoding = "utf8")
cities = list(map(lambda s: s.strip().lower(), citiesF.readlines()))

usedCities = []
currentCity = [" ", -1]
usedLetters = ["ь", "ъ"]

startPhrases = ["Ты начинаешь", "Начинай", "Настарт-внимание-маррррррш!!"]
currentPhrases = ["Ты начинаешь", "Ходи", "Твой ход"]
falsePhrases = ["Точно без ошибок написано? Не засчитываю", "Не знаю о таком", "Мимо!", "Только русские города, помнишь?"]
exitPhrases = ["я устал, я ухожу", "я устал", "отстань", "уйди противный", "отвали", "задолбал", "бесишь", "q", "Q", "отвянь"]
usedPhrases = ["Повторяешься!", "Было!"]
botPhrases = ["окей, мой тебе ответ - ", "а я тебе - "]


def botAnswer(personCity):
    indent = -1
    if personCity[-1] in usedLetters:
        indent = -2
    cityPool = list()
    for city in cities:
        if city not in usedCities and city[0].lower() == personCity[indent]:
            cityPool.append(city)
    try:
        usedCity = cityPool[random.randint(0, len(cityPool)-1)]
        usedCities.append(usedCity)
        # print(cityPool)
        return [usedCity, len(cityPool)]
    except:
        return ["сдаюсь!", 0]

print('''Сыграем в города?
        Правила простые - каждый игрок должен сказать название города, которое начинается на последнюю букву города от предыдущего игрока.
        Чтобы прекратить игру введи "я устал, я ухожу".
        Только русские города, патриот ты или как?
''')


continueGame = True

quantity = 1

while continueGame:
    if quantity == 1:
        personCity = (input(startPhrases[random.randint(1, len(startPhrases)-1)] + "\n").strip().lower())
    else:
        personCity = (input(currentPhrases[random.randint(1, len(currentPhrases)-1)] + "\n").strip().lower())

    if not personCity:
        print ("не нажимай enter всуе")
        continue

    if personCity.lower() in exitPhrases:
        print("Ну и ладно, больно надо..." if quantity <= 10 else "неплохо сыграли, возвращайся еще!")
        continueGame = False
        continue

    if currentCity[0][-1].lower() in usedLetters:
        indent = -2
    else:
        indent = -1

    if personCity[0].lower() != currentCity[0][indent] and quantity > 1:
        print(indent, currentCity[0][indent])
        print("Название города должно начинаться на \"" + currentCity[0][indent].title() + "\"")
        continue

    elif personCity.lower() in cities and personCity.lower() not in usedCities:
        usedCities.append(personCity.lower())
        botAns = botAnswer(personCity)
        currentCity = botAns
        if botAns[1] == 0:
            print("Ты хорошо играешь =)")
            continueGame = False
            continue

        print(botPhrases[random.randint(0,len(botPhrases)-1)] + botAns[0])
        quantity += 1

        if botAns[1] == 1:
            addUsedLetter = input("похоже, я больше не знаю городов на букву \"" + personCity[-1] + "\" внести её в список букв, которые не используем как начальные? да/нет \n")
            if addUsedLetter in ["да", "д"]:
                usedLetters.append(personCity[-1])
                print('ок, занес. Сейчас если город заканчивается на эту букву, ты придумываешь на стоящую перед ней')

        continue

    elif personCity.lower() in usedCities:
        print(usedPhrases[random.randint(0, len(usedPhrases)-1)]+" ")
        continue
    else:
        print(falsePhrases[random.randint(0, len(falsePhrases)-1)]+" ")
        continue


citiesF.close()

# Пофиксить:
# 1) (done) проверка ввода первой буквы у пользователя
# 2) (done) говорить, когда город повторяется
# 3) (done) и если городов на "Ы" больше нет - говорить, что используем предыдущую букву
# 4) (done) проверять на пустой ввод (показывать спец. сообщение) и strip-пать (убирать пробелы перед и после)
# 5) (done) назвать переменные чуть осмысленнее и без транслитерации: continueGame, quantity, indent
# 6) (done) рандномизировать ответы бота (выбор городов по первой букве, а не по порядку)
# 7) впилить его в телеграм-бот
# 8) сделать возможность выбора категорий слов
# 9) перевод на английский язык
# 10)(done) Выходить из цикла сразу после "я устал, я ухожу"
# 11) (done...вроде) Что не так с Йошкар-ола?
# 12) (done) сделать доп.обработку по унификации городов

