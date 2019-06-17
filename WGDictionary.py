import random

class wgDictionary():

    usedLetters = []
    dictionary = []
    tempDictionary = []
    usedWords = []
    currentWord = ""
    alphabet = ""

    def __init__(self, path, lang):
        self.path = path
        self.lang = lang

    def makeDictionary(self):
        FwgDictionary = open(self.path, "r", encoding = "utf8")
        self.tempDictionary = list(map(lambda s: s.strip().lower(), FwgDictionary.readlines()))

        self.initLetters()
        FwgDictionary.close()
        return self.dictionary

    def initLetters(self):
        if self.lang == "EN":
            self.alphabet = "abcdefghijklmnopqrstuvwxyz"

        if self.lang == "RU":
            self.alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"

        for letter in self.alphabet:
            self.dictionary.append([])

        for word in self.tempDictionary:
            position = self.alphabet.index(word[0:1].lower())
            self.dictionary[position].append(word)

        for i in range(len(self.dictionary)):
            if len(self.dictionary[i]) == 0:
                self.usedLetters.append(self.alphabet[i:i+1])

    def addUsedLetters(self, letter):
        self.usedLetters.append(letter)

        if self.lang == "RU":
            print("буква " + letter.title() + " была добавлена в использованные. Я больше не знаю слов, начинающихся на эту букву")

        if self.lang == "EN":
            print("letter " + letter.title() + " was added to used letters. I don't know any word starting from this letter.")

    def checkLetter(self, letter):
        index = self.alphabet.find(letter.lower())
        if len(self.dictionary[index]) == 0:
            self.addUsedLetters(letter)

class languages():
    startPhrases = []
    yourTurnPhrases = []
    falsePhrases = []
    firstinput = ""



    def __init__(self, lang):
        self.lang = lang
        # self.theme = theme
        if self.lang == "RU":
            self.firstinput = "Выбери тип игры - города/животные\n"
        else:
            self.firstinput = "Select the type of the game - cities/animals\n"


    def printDescription(self):

        if self.lang == "RU":
            print('''Правила простые - каждый игрок должен сказать слово, которое начинается на последнюю букву слова предыдущего игрока. 
Чтобы прекратить игру введи "я устал, я ухожу".''')

        elif self.lang == "EN":
            print('''Let's play!
The rules are simple. You should type a word, which begins with the last letter of the previous word.
Type "Q" to stop the game.
            ''')

    def initStartPhrases(self):
        if self.lang == "RU":
            self.startPhrases = ["Ты начинаешь", "Начинай", "Настарт-внимание-маррррррш!!", "Давай же, поехали!"]

        elif self.lang == "EN":
            self.startPhrases = ["Go!", "You start", "Ready - steady - go!"]

        return(self.startPhrases[random.randint(0,len(self.startPhrases)-1)] + "\n")

    def giveYourTurnPhrases(self):
        if self.lang == "RU":
            self.yourTurnPhrases = ["тебя ждем...", "ходи!", "твой ход..."]

        elif self.lang == "EN":
            self.yourTurnPhrases = ["your turn!", "I'll wait...", "you're up!", "your round", "you're go"]

        return(self.startPhrases[random.randint(0,len(self.startPhrases)-1)] + "\n")

continueGame = True
quantity = 0

lang = input("Выбери язык/Select the language - RU/EN\n")
if lang[0] in ['R','r','р','Р']:
    gameLanguage = languages("RU")
else:
    gameLanguage = languages("EN")

type = input(gameLanguage.firstinput)

if type[0] in ['г', 'Г']:
    words = wgDictionary("data/citiesRU.txt", "RU")
elif type[0] in ['ж','Ж']:
    words = wgDictionary("data/animalsRU.txt", "RU")
elif type[0] in ['c','C']:
    words = wgDictionary("data/citiesEN.txt", "EN")
elif type[0] in ['a', 'A']:
    words = wgDictionary("data/animalsEN.txt", "EN")

words.makeDictionary()
gameLanguage.printDescription()

while continueGame:
    if quantity == 0:
        personWord = input(gameLanguage.initStartPhrases())
    else:
        personWord = input(gameLanguage.giveYourTurnPhrases())










