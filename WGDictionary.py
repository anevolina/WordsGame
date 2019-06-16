class wgDictionary():

    usedLetters = []
    dictionary = []
    tempDictionary = []
    usedWords = []
    currentWord = " "
    dicLetters = ""

    def __init__(self, path, lang):
        self.path = path
        self.lang = lang


    def makeDictionary(self):
        FwgDictionary = open(self.path, "r", encoding = "utf8")
        self.tempDictionary = list(map(lambda s: s.strip().lower(), FwgDictionary.readlines()))

        self.initLetters()
        return self.dictionary

    def initLetters(self):
        if self.lang == "EN":
            self.dicLetters == "abcdefghijklmnopqrstuvwxyz"

        if self.lang == "RU":
            self.dicLetters = "абвгдежзийклмнопрстуфхцчшщъыьэюя"

        for letter in self.dicLetters:
            self.dictionary.append([])

        for word in self.tempDictionary:
            position = self.dicLetters.index(word[0:1])
            self.dictionary[position].append(word)

        for i in range(len(self.dictionary)):
            if len(self.dictionary[i]) == 0:
                self.usedLetters.append(self.dicLetters[i:i+1])
                # self.addUsedLetters(dicLetters[i:i+1])

    def addUsedLetters(self, letter):
        self.usedLetters.append(letter)

        if self.lang == "RU":
            print("буква " + letter.title() + " была добавлена в использованные. Я больше не знаю слов, начинающихся на эту букву")

        if self.lang == "EN":
            print("letter " + letter.title() + " was added to used letters. I don't know any word starting from this letter.")

    def checkLetter(self, letter):
        index = self.dicLetters.find(letter.lower())
        if len(self.dictionary[index]) == 0:
            self.addUsedLetters(letter)



cities = wgDictionary("data/cities.txt", "RU")
cities.makeDictionary()
cities.checkLetter("Ъ")








