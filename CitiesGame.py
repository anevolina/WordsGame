import random

citiesF = open("cities.txt", "r", encoding = "utf8")
cities = list(map(lambda s: s.strip(), citiesF.readlines()))

usedCities = []
currentCity = ""

def botAnswer(personCity):
    otst = -1
    if personCity[-1] == "ь" or personCity[-1] == "ъ":
        otst = -2
    for city in cities:
        if city not in usedCities:
            if city[0].lower() == personCity[otst]:
                usedCities.append(city)
                return city
    return "сдаюсь!"

print ('''Сыграем в города?
        Правила простые - каждый игрок должен сказать название города, которое начинается на последнюю букву города от предыдущего игрока.
        Чтобы прекратить игру введи "я устал, я ухожу".
        Только русские города, патриот ты или как?
''')

phrases = ["Ты начинаешь", "Ходи", "Твой ход"]
falsePhrases = ["Точно без ошибок написано? Не засчитываю", "Не знаю о таком", "Мимо!"]
usedPhrases = ["Повторяешься!", "Было!"]

cont = True

kol = 1

while cont:
    if kol == 1:
        personCity = input(phrases[0]+"\n").lower()
    else:
        personCity = input(phrases[random.randint(1,len(phrases)-1)]+ "\n").lower()

    if personCity == "я устал, я ухожу" or personCity == "q":
        print ("Ну и ладно, больно надо..." if kol <= 10 else "неплохо сыграли, возвращайся еще!")
        cont = False

    if personCity.title() in cities and personCity.title() not in usedCities:
        usedCities.append(personCity.title())
        botAns = botAnswer(personCity)
        if botAns == "сдаюсь!":
            print ("неплохо играешь!")
            cont = False
        print ("окей, мой тебе ответ - " + botAns)
        kol += 1
        continue

    elif personCity.title() in usedCities:
        print (usedPhrases[random.randint(0, len(usedPhrases)-1)]+" ")
        continue
    else:
        print (falsePhrases[random.randint(0, len(falsePhrases)-1)]+" ")
        continue


citiesF.close()

# Пофиксить:
# 1) проверка ввода первой буквы у пользователя
# 2) говорить, когда город повторяется (done)
# 3) и если городов на "Ы" больше нет - говорить, что используем предыдущую букву
# 4) проверять на пустой ввод (показывать спец. сообщение) и strip-пать (убирать пробелы перед и после)
# 5) назвать переменные чуть осмысленнее и без транслитерации: cont, kol, otst
# 6) рандномизировать ответы бота
# 7) впилить его в телеграм-бот
# 8) сделать возможность выбора категорий слов
# 9) перевод на английский язык

