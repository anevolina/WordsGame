import random
from phrases import Phrases
from dictionary import WordsGameDictionary


class WordsGameBot():

    def __init__(self, path, lang='RU'):
        self.phrases = Phrases(lang)
        self.words = WordsGameDictionary(path, lang)
        self.continue_game = True
        self.additional_info = ''
        self.current_word = ' '
        self.quantity = 0

    def is_game_over(self):
        if self.current_word[-1] in self.words.used_letters and \
                self.current_word[-2] in self.words.used_letters:
            self.continue_game = False
            return True
        else:
            return False

    def is_correct_first_letter(self, person_word, indent):
        if person_word[0].lower() != self.current_word[indent] and self.quantity > 0:
            return False
        return True

    def is_bot_knows_person_word(self, person_word):
        index_of_letter = self.return_index_of_letter(person_word[0].lower())
        if person_word.lower() in self.words.dictionary[index_of_letter]:
            return True
        else:
            return False

    def is_person_word_used(self, person_word):
        if person_word.lower() in self.words.used_words:
            return True
        else:
            return False

    def return_index_of_letter(self, letter):
        index_of_letter = self.words.alphabet.find(letter.lower())
        return index_of_letter

    def add_used_word_del_from_dic(self, word):
        self.words.used_words.append(word.lower())
        index_of_letter = self.return_index_of_letter(word[0])
        self.words.dictionary[index_of_letter].remove(word.lower())

    def check_word_and_letters(self, word):
        if not self.words.is_know_words_on_letter(word[0]):
            self.additional_info += self.phrases.used_letter_was_added(word[0].lower()) + '\n'
        if self.is_game_over():
            self.additional_info = self.phrases.give_game_over_phrases() + '\n'

    def restart_bot(self, path, lang='RU'):
        self.__init__(path, lang)


    # define bot's answers to the input
    def bot_answer_is(self, person_word):

        # if user wants to stop the game
        if person_word in self.phrases.user_exit_phrases:
            self.continue_game = False
            return [self.phrases.give_exit_phrases(self.quantity)]

        # if user just pushed enter without typing
        if not person_word:
            return [self.phrases.give_enter_phrases()]

        # Define an indent for the future checking
        if self.current_word[-1] in self.words.used_letters:
            indent = -2
        else:
            indent = -1

        # Check if last two letters was used (no more words started from them are exist in our dictionary)
        # we have to stop the whole game
        if self.is_game_over():
            return [self.phrases.give_game_over_phrases()]


        # Check if user's word started from correct letter, according to intend
        if not self.is_correct_first_letter(person_word, indent):
            return [self.phrases.give_false_letter_phrases(self.current_word[indent])]

        # Check if user's word already used
        if self.is_person_word_used(person_word):
            return [self.phrases.give_used_phrases()]


        # Check if bot knows user's word then return an answer
        if self.is_bot_knows_person_word(person_word):
            self.additional_info = ''
            self.add_used_word_del_from_dic(person_word)
            self.check_word_and_letters(person_word)
            self.quantity += 1
            self.current_word = self.bot_word(person_word)

            if self.current_word == "GiveUp":
                self.continue_game = False
                return [self.phrases.give_game_over_phrases()]

            self.check_word_and_letters(self.current_word)
            if self.continue_game:
                return [self.additional_info, self.current_word]
            else:
                return [self.current_word, self.additional_info]

        else:
            return [self.phrases.give_false_phrases()]

    def bot_word(self, person_word):
        if person_word[-1] in self.words.used_letters:
            indent = -2
        else:
            indent = -1

        index_of_letter = self.return_index_of_letter(person_word[indent])
        try:
            bot_word = self.words.dictionary[index_of_letter][random.randint(0, len(self.words.dictionary
                                                                                    [index_of_letter]) - 1)]
            self.add_used_word_del_from_dic(bot_word)

            return bot_word.title()
        except ValueError:
            return "GiveUp"


# Test class and whole game
#
# my_bot = WordsGameBot('data/citiesForTest.txt')
#
# while my_bot.continue_game:
#     person_word = input('Введи слово\n')
#     bot_answer = my_bot.bot_answer_is(person_word.strip())
#     print(bot_answer)