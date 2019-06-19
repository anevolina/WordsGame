import random
from colorama import  Fore, Back, Style
import os


class WGDictionary():

    usedLetters = []
    dictionary = []
    tempDictionary = []
    usedWords = []
    alphabet = ""

    def __init__(self, path, lang):
        self.path = path
        self.lang = lang

    def make_dictionary(self):
        FWGDictionary = open(self.path, "r", encoding = "utf8")
        self.tempDictionary = list(map(lambda s: s.strip().lower(), FWGDictionary.readlines()))

        self.init_letters()
        FWGDictionary.close()
        return self.dictionary

    def init_letters(self):
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

    def add_used_letters(self, letter):
        self.usedLetters.append(letter)

        if self.lang == "RU":
            print("буква " + letter.title() + " была добавлена в использованные. Я больше не знаю слов, начинающихся на эту букву")

        if self.lang == "EN":
            print("letter " + letter.title() + " was added to used letters. I don't know any word starting from this letter.")

    def check_letter(self, letter):
        index = self.alphabet.find(letter.lower())

        if len(self.dictionary[index]) == 0:
            self.add_used_letters(letter.lower())


    def return_index_of_letter(self, letter):
       return self.alphabet.find(letter.lower())

    def bot_answer(self, word):
        if word[-1] in self.usedLetters:
            indent = -2
        else:
            indent = -1
        indexOfLetter = self.return_index_of_letter(word[indent])
        try:
            botWord = self.dictionary[indexOfLetter][random.randint(0, len(self.dictionary[indexOfLetter]) - 1)]
            self.usedWords.append(botWord.lower())
            self.dictionary[indexOfLetter].remove(botWord.lower())
            self.check_letter(botWord[0])
            return botWord
        except ValueError:
            return "GiveUp"





class Languages():

    firstinput = ""

    def __init__(self, lang):
        self.lang = lang
        # self.theme = theme
        if self.lang == "RU":
            self.firstinput = "Выбери тип игры - города/животные\n"
        else:
            self.firstinput = "Select the type of the game - cities/animals\n"


    def print_description(self):

        if self.lang == "RU":
            print('''Правила простые - каждый игрок должен сказать слово, которое начинается на последнюю букву слова предыдущего игрока. 
Чтобы прекратить игру введи "я устал, я ухожу".''')

        elif self.lang == "EN":
            print('''Let's play!
The rules are simple. You should type a word, which begins with the last letter of the previous word.
Type "Q" to stop the game.
            ''')

    def give_start_phrases(self):
        if self.lang == "RU":
            startPhrases = ["Ты начинаешь", "Начинай", "Настарт-внимание-маррррррш!!", "Давай же, поехали!"]

        elif self.lang == "EN":
            startPhrases = ["Go!", "You start", "Ready - steady - go!"]

        return(startPhrases[random.randint(0,len(startPhrases)-1)] + "\n")

    def give_your_turn_phrases(self):
        if self.lang == "RU":
            yourTurnPhrases = ["тебя ждем...", "ходи!", "твой ход..."]
            nextLetterPhrase = " думай слово на букву "

        elif self.lang == "EN":
            yourTurnPhrases = ["your turn!", "I'll wait...", "you're up!", "your round", "you're go"]
            nextLetterPhrase = " type word starting from "

        return(yourTurnPhrases[random.randint(0,len(yourTurnPhrases)-1)] + nextLetterPhrase)

    def give_false_phrases(self):
        if self.lang == "RU":
            falsePhrases = ["точно без ошибок написано? Не засчитываю", "не знаю о чем ты", "мимо!"]

        elif self.lang == "EN":
            falsePhrases = ["are you sure?", "don't know what are you talking about",
                                 "maybe there is a typo mistake? Doesn't count!",
                                 "hmmm... doesn't count", "input something else"]

        return (falsePhrases[random.randint(0, len(falsePhrases) - 1)] + "\n")

    def give_used_phrases(self):
        if self.lang == "RU":
            usedPhrases = ["повторяешься!", "было!"]

        elif self.lang == "EN":
            usedPhrases = ["used!", "was used! input something  else!"]

        return (usedPhrases[random.randint(0, len(usedPhrases) - 1)] + "\n")

    def give_bot_phrases(self):
        if self.lang == "RU":
            botPhrases = ["окей, мой тебе ответ - ", "а я тебе - "]

        elif self.lang == "EN":
            botPhrases = ["and my answer is ", "my word is "]

        return (botPhrases[random.randint(0, len(botPhrases) - 1)] + "\n")

    def give_enter_phrases(self):
        if self.lang == "RU":
            enterPhrase = "не нажимай Enter всуе!"

        elif self.lang == "EN":
            enterPhrase = "don't press Enter without a word!"

        return enterPhrase

    def give_exit_phrases(self, quantity):
        if self.lang == "RU":
            exitPhrase1 = "Ну и ладно, больно надо..."
            exitPhrase2 = "неплохо сыграли, возвращайся еще!"

        elif self.lang == "EN":
            exitPhrase1 = "Well, okay, it hurts..."
            exitPhrase2 = "nice played! Come back again!"

        return exitPhrase1 if quantity < 10 else exitPhrase2

    def give_game_over_phrases(self):
        if self.lang == "RU":
            gameOverPhrase = "прекращаем игру по техническим причинам - я больше не знаю слов, начинающихся на одну из последних двух букв"

        elif self.lang == "EN":
            gameOverPhrase = "game over according to technical issues - I don't know more words starting from the last two letters"

        return gameOverPhrase

    def give_false_letter_phrases(self, letter):
        if self.lang == "RU":
            falseLetterPhrase = "Слово должно начинаться на букву \"" + letter.title() + "\""

        elif self.lang == "EN":
            falseLetterPhrase = "Yor word should start with \"" + letter.title() + "\""

        return falseLetterPhrase


exitPhrases = ["я устал, я ухожу", "я устал", "отстань", "уйди противный", "отвали", "задолбал", "бесишь", "отвянь",
               "q", "Q", "quit", "I'm tired", "tired", "fuck off"]

continueGame = True
currentWord = "  "
quantity = 0

lang = input("Выбери язык/Select the language - RU/EN\n")
if lang[0] in ['R', 'r', 'р', 'Р']:
    gameLanguage = Languages("RU")
else:
    gameLanguage = Languages("EN")

type = input(gameLanguage.firstinput)

if type[0] in ['г', 'Г']:
    words = WGDictionary(os.path.join("data", "citiesRU.txt"), "RU")
elif type[0] in ['ж', 'Ж']:
    words = WGDictionary(os.path.join("data", "animalsRU.txt"), "RU")
elif type[0] in ['c', 'C']:
    words = WGDictionary(os.path.join("data", "citiesEN.txt"), "EN")
elif type[0] in ['a', 'A']:
    words = WGDictionary(os.path.join("data", "animalsEN.txt"), "EN")
else:
    words = WGDictionary(os.path.join("data", "citiesForTest.txt"), "RU")

words.make_dictionary()
gameLanguage.print_description()

while continueGame:


    if currentWord[-1] in words.usedLetters and currentWord[-2] in words.usedLetters:
        print(gameLanguage.give_game_over_phrases())
        continueGame = False
        continue

    if currentWord[-1] in words.usedLetters:
        indent = -2
    else:
        indent = -1


    if quantity == 0:
        personWord = input(gameLanguage.give_start_phrases() + currentWord[indent].title()+"\n").strip()
    else:
        personWord = input(gameLanguage.give_your_turn_phrases()+ currentWord[indent].title()+"\n").strip()

    if not personWord:
        print(gameLanguage.give_enter_phrases())
        continue

    if personWord.lower() in exitPhrases:
        continueGame = False
        print(gameLanguage.give_exit_phrases(quantity))
        continue

    if personWord[0].lower() != currentWord[indent] and quantity > 0:

        print(gameLanguage.give_false_letter_phrases(currentWord[indent]))
        continue

    indexOfLetter = words.return_index_of_letter(personWord[0])
    if personWord.lower() in words.dictionary[indexOfLetter]:
        words.usedWords.append(personWord.lower())
        words.dictionary[indexOfLetter].remove(personWord.lower())
        words.check_letter(personWord[0])
        quantity += 1
        currentWord = words.bot_answer(personWord)

        if currentWord == "GiveUp":
            print(gameLanguage.give_game_over_phrases())
            continueGame = False
            continue

        print(gameLanguage.give_bot_phrases())
        print(Fore.RED + currentWord.title())
        print(Style.RESET_ALL)

    elif personWord.lower() in words.usedWords:
            print(gameLanguage.give_used_phrases())
    else:
        print(gameLanguage.give_false_phrases())























