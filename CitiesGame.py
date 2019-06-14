import random
from colorama import  Fore, Back, Style

citiesF = open("cities.txt", "r", encoding = "utf8")
cities = list(map(lambda s: s.strip().lower(), citiesF.readlines()))

usedCities = []
currentCity = [" ", -1]
usedLetters = ["ь", "ъ"]

startPhrases = ["Ты начинаешь", "Начинай", "Настарт-внимание-маррррррш!!", "Давай же, поехали!"]
currentPhrases = ["тебя ждем...", "ходи!", "твой ход..."]
falsePhrases = ["точно без ошибок написано? Не засчитываю", "не знаю о таком", "мимо!", "только русские города, помнишь?"]
exitPhrases = ["я устал, я ухожу", "я устал", "отстань", "уйди противный", "отвали", "задолбал", "бесишь", "q", "Q", "отвянь"]
usedPhrases = ["повторяешься!", "было!"]
botPhrases = ["окей, мой тебе ответ - ", "а я тебе - "]


def botAnswer(personCity):

    cityPool = findAvailableCities(personCity)

    try:
        usedCity = cityPool[random.randint(0, len(cityPool)-1)]
        isUsedLetter = False
        usedCities.append(usedCity)
        cities.remove(usedCity.lower())
        if len(cityPool) == 1:
            addUsedLetter(usedCity[0], True)
            isUsedLetter = True
        return [usedCity, isUsedLetter]
    except:
        return ["сдаюсь!", True]

def findAvailableCities(currentCity):
    indent = -1
    if currentCity[-1] in usedLetters:
        indent = -2
    cityPool = list()
    for city in cities:
        if city[0].lower() == currentCity[indent]:
            cityPool.append(city)
    # print(cityPool)

    return cityPool

def addUsedLetter(usedLetter, isBot):
        usedLetters.append(usedLetter)
        # print("буква \"" + usedLetter + "\" была добавлена в использованные - я больше не знаю городв, начинающихся на эту букву.\n")



print('''Сыграем в города?
        Правила простые - каждый игрок должен сказать название города, которое начинается на последнюю букву города от предыдущего игрока.
        Чтобы прекратить игру введи "я устал, я ухожу".
        Только русские города, патриот ты или как?
''')


continueGame = True

quantity = 1

while continueGame:

    if currentCity[0][-1] in usedLetters and currentCity[0][-2] in usedLetters:
        print("прекращаем игру по техническим причинам - я больше не знаю городов, начинающихся на одну из последних двух букв")
        continueGame = False
        continue


    if currentCity[0][-1].lower() in usedLetters:
        indent = -2
    else:
        indent = -1

    if quantity == 1:
        personCity = (input(startPhrases[random.randint(1, len(startPhrases)-1)] + "\n").strip().lower())
    else:
        personCity = (input(currentPhrases[random.randint(1, len(currentPhrases)-1)] + " думай город на букву \"" + currentCity[0][indent] + "\"\n").strip().lower())


    if not personCity:
        print ("не нажимай Enter всуе")
        continue

    if personCity.lower() in exitPhrases:
        print("Ну и ладно, больно надо..." if quantity <= 10 else "неплохо сыграли, возвращайся еще!")
        continueGame = False
        continue



    if personCity[0].lower() != currentCity[0][indent] and quantity > 1:
        print("Название города должно начинаться на \"" + currentCity[0][indent].title() + "\"")
        continue


    elif personCity.lower() in cities:
        usedCities.append(personCity.lower())
        cities.remove(personCity.lower())
        checkLetter = findAvailableCities(currentCity[0])

        if len(checkLetter) == 0 and quantity > 1 :
            # print(currentCity)
            addUsedLetter(currentCity[0][indent], False)
            print("буква \"" + currentCity[0][indent] + "\" была добавлена в неиспользуемые - я больше не знаю городв, начинающихся на эту букву.\n")
        botAns = botAnswer(personCity)

        currentCity = botAns
        if botAns[0] == "сдаюсь!":
            print("Сдаюсь! Я больше не знаю городов, начинающихся на оддну из последних двух букв. Ты хорошо играешь =)")
            continueGame = False
            continue

        print(botPhrases[random.randint(0, len(botPhrases)-1)])
        print(Fore.RED + botAns[0].title())
        print(Style.RESET_ALL)

        if botAns[1]:
            print("буква \"" + botAns[0][0] + "\" была добавлена в неиспользуемые - я больше не знаю городв, начинающихся на эту букву.\n")
        quantity += 1

        continue

    elif personCity.lower() in usedCities:
        print(usedPhrases[random.randint(0, len(usedPhrases)-1)]+" \n")
        continue
    else:
        print(falsePhrases[random.randint(0, len(falsePhrases)-1)]+" \n")
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
# 13) (done) вывод технических принтов убрать
# 14) (done) бот выводит города с маленькой буквы
# 15) (done) убирать редкие конечные буквы самостоятельно без возможности выбора?
# 16) (done) напоминать, на какую букву отвечает пользователь
# 17) (done) убирать использованную букву после ввода пользователя
# 18) Баг - не проверяется первая буква первого слова пользователя (она может вылететь после первого же слова ытык-кюель) проверять, чтобы городов на эту букву было минимум 2?
# или сделать проверку cityPool по букве, а не по слову?

