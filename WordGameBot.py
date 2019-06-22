import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from dotenv import load_dotenv
import logging
import os
from os.path import join, dirname

from WGMain import WGDictionary, Languages

# start logging everything...as like I know where to find all this logs...
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

# Load .env & token for the bot
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)
TLGR_TOKEN = os.environ.get('TLGR_TOKEN')

# Initialize updater and dispatcher... as like I know what it is
updater = Updater(token=TLGR_TOKEN)
dispatcher = updater.dispatcher

# load dictionary
words = WGDictionary(os.path.join("data", "citiesRU.txt"), "RU")
words.make_dictionary()

# define global variables
game_language = Languages("RU")
continue_game = True
currentWord = "  "
quantity = 0


# define reaction to /start command in tlgr
def start_callback(bot, update):
    update.message.reply_text(game_language.give_description())

# define reaction to person input
def answer(bot, update):
    bot_answer = whole_game(update.message.text)
    bot.send_message(chat_id=update.message.chat_id, text=bot_answer)

# define bot's answers to the input
def whole_game(person_word):

    global quantity, currentWord, words

    if currentWord[-1] in words.usedLetters and currentWord[-2] in words.usedLetters:
        return game_language.give_game_over_phrases()

    if currentWord[-1] in words.usedLetters:
        indent = -2
    else:
        indent = -1

    if person_word[0].lower() != currentWord[indent] and quantity > 0:
        return game_language.give_false_letter_phrases(currentWord[indent])

    index_of_letter = words.return_index_of_letter(person_word[0])
    if person_word.lower() in words.dictionary[index_of_letter]:
        words.usedWords.append(person_word.lower())
        words.dictionary[index_of_letter].remove(person_word.lower())
        words.check_letter(person_word[0])
        quantity += 1
        currentWord = words.bot_answer(person_word)

        if currentWord == "GiveUp":
            return game_language.give_game_over_phrases()

        return game_language.give_bot_phrases() + currentWord.title()

    elif person_word.lower() in words.usedWords:
        return game_language.give_used_phrases()
    else:
        return game_language.give_false_phrases()


# define all handlers
answer_handler = MessageHandler(Filters.text, answer)
start_handler = CommandHandler("start", start_callback)

# adding handlers to our dipatcher
dispatcher.add_handler(start_handler)
dispatcher.add_handler(answer_handler)

# and start the bot...
updater.start_polling()
