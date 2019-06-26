import random


class Phrases():

    def __init__(self, lang="RU"):
        self.lang = lang
        self.first_input = ""
        # self.theme = theme
        if self.lang == "RU":
            self.first_input = "Выбери тип игры - города/животные\n"
            self.user_exit_phrases = ['в', 'й']
        else:
            self.first_input = "Select the type of the game - cities/animals\n"
            self.user_exit_phrases = ['q']

    def give_description(self):

        if self.lang == "RU":
            return('''Правила простые - каждый игрок должен ввести город, название которого начинается на последнюю букву города предыдущего игрока.\nНачинай!''')

        elif self.lang == "EN":
            return('''Let's play!
The rules are simple. You should type a word, which begins with the last letter of the previous word.
Type "Q" to stop the game.
            ''')

    def give_start_phrases(self):
        if self.lang == "RU":
            start_phrases = ["Ты начинаешь", "Начинай", "Настарт-внимание-маррррррш!!", "Давай же, поехали!"]

        elif self.lang == "EN":
            start_phrases = ["Go!", "You start", "Ready - steady - go!"]

        return(start_phrases[random.randint(0,len(start_phrases)-1)] + "\n")

    def give_your_turn_phrases(self):
        if self.lang == "RU":
            your_turn_phrases = ["тебя ждем...", "ходи!", "твой ход..."]
            next_letter_phrase = " думай слово на букву "

        elif self.lang == "EN":
            your_turn_phrases = ["your turn!", "I'll wait...", "you're up!", "your round", "you're go"]
            next_letter_phrase = " type word starting from "

        return(your_turn_phrases[random.randint(0,len(your_turn_phrases)-1)] + next_letter_phrase)

    def give_false_phrases(self):
        if self.lang == "RU":
            false_phrases = ["точно без ошибок написано? Не засчитываю", "не знаю о чем ты", "мимо!"]

        elif self.lang == "EN":
            false_phrases = ["are you sure?", "don't know what are you talking about",
                                 "maybe there is a typo mistake? Doesn't count!",
                                 "hmmm... doesn't count", "input something else"]

        return (false_phrases[random.randint(0, len(false_phrases) - 1)] + "\n")

    def give_used_phrases(self):
        if self.lang == "RU":
            used_phrases = ["повторяешься!", "было!"]

        elif self.lang == "EN":
            used_phrases = ["used!", "was used! input something  else!"]

        return (used_phrases[random.randint(0, len(used_phrases) - 1)] + "\n")

    def give_bot_phrases(self):
        if self.lang == "RU":
            bot_phrases = ["окей, мой тебе ответ - ", "а я тебе - "]

        elif self.lang == "EN":
            bot_phrases = ["and my answer is ", "my word is "]

        return (bot_phrases[random.randint(0, len(bot_phrases) - 1)] + "\n")

    def give_enter_phrases(self):
        if self.lang == "RU":
            enter_phrases = "не нажимай Enter всуе!"

        elif self.lang == "EN":
            enter_phrases = "don't press Enter without a word!"

        return enter_phrases

    def give_exit_phrases(self, quantity):
        if self.lang == "RU":
            exit_phrase_too_early = "Ну и ладно, больно надо..."
            exit_phrase_well_done = "неплохо сыграли, возвращайся еще!"

        elif self.lang == "EN":
            exit_phrase_too_early = "Well, okay, it hurts..."
            exit_phrase_well_done = "nice played! Come back again!"

        return exit_phrase_too_early if quantity < 10 else exit_phrase_well_done

    def give_game_over_phrases(self):
        if self.lang == "RU":
            game_over_phrase = "прекращаем игру по техническим причинам - я больше не знаю слов, начинающихся на одну из последних двух букв"

        elif self.lang == "EN":
            game_over_phrase = "game over according to technical issues - I don't know more words starting from the last two letters"

        return game_over_phrase

    def give_false_letter_phrases(self, letter):
        if self.lang == "RU":
            false_letter_phrase = "Слово должно начинаться на букву \"" + letter.title() + "\""

        elif self.lang == "EN":
            false_letter_phrase = "Yor word should start with \"" + letter.title() + "\""

        return false_letter_phrase

    def used_letter_was_added(self,letter):
        if self.lang == "RU":
            added_letter_phrase = (
                "буква " + letter.title() + " была добавлена в использованные. Я больше не знаю слов, начинающихся на эту букву")

        if self.lang == "EN":
            added_letter_phrase = (
                "letter " + letter.title() + " was added to used letters. I don't know any word starting from this letter.")
        return added_letter_phrase