
class WordsGameDictionary():

    def __init__(self, path, lang):
        self.path = path
        self.lang = lang
        self.used_letters = []
        self.alphabet = ''
        self.used_words = []
        self.dictionary = []

        self.make_dictionary()


    # Initialize the dictionary from the file
    def make_dictionary(self):
        file_dictionary = open(self.path, "r", encoding="utf8")
        temp_dictionary = list(map(lambda s: s.strip().lower(), file_dictionary.readlines()))

        self.init_letters(temp_dictionary)
        file_dictionary.close()
        return self.dictionary

    # Split words from the file by alphabet
    def init_letters(self, temp_dictionary):
        if self.lang == "EN":
            self.alphabet = "abcdefghijklmnopqrstuvwxyz"

        if self.lang == "RU":
            self.alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"

        for letter in self.alphabet:
            self.dictionary.append([])

        for word in temp_dictionary:
            position = self.alphabet.index(word[0:1].lower())
            self.dictionary[position].append(word)

        for i in range(len(self.dictionary)):
            if len(self.dictionary[i]) == 0:
                self.used_letters.append(self.alphabet[i:i+1])

    # Check if it's still any word in dictionary starting from this letter
    def is_know_words_on_letter(self, letter):
        index = self.alphabet.find(letter.lower())

        if len(self.dictionary[index]) == 0:
            self.used_letters.append(letter.lower())
            return False

        return True
