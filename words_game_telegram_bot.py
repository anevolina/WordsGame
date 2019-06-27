import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from dotenv import load_dotenv
import logging
import os
from os.path import join, dirname

from bot_answers import WordsGameBot

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

# Initialize bot collection
bot_collection = {}

def start_bot(user_id):
    if user_id in bot_collection:
        bot_collection[user_id].restart_bot('data/citiesRU.txt')
    else:
        new_bot = WordsGameBot('data/citiesRU.txt')
        bot_collection[user_id] = new_bot


# define reaction to /start command in tlgr
def start_callback(bot, update):
    user_id = update.message.from_user.id
    start_bot(user_id)
    update.message.reply_text(bot_collection[user_id].phrases.give_description())


def restart_callback(bot, update):
    user_id = update.message.from_user.id
    start_bot(user_id)
    update.message.reply_text(bot_collection[user_id].phrases.restart_phrases())


# define reaction to person input
def answer(bot, update):
    user_id = update.message.from_user.id
    if user_id not in bot_collection:
        start_bot(user_id)
    bot_answers = bot_collection[user_id].bot_answer_is(update.message.text.strip())
    for bot_answer in bot_answers:
        if not bot_answer:
            continue
        bot.send_message(chat_id=update.message.chat_id, text=bot_answer)

    if bot_collection[user_id].continue_game == False:
        start_bot(user_id)



# define all handlers
answer_handler = MessageHandler(Filters.text, answer)
start_handler = CommandHandler("start", start_callback)
restart_handler = CommandHandler('restart', restart_callback)

# adding handlers to our dispatcher
dispatcher.add_handler(start_handler)
dispatcher.add_handler(answer_handler)
dispatcher.add_handler(restart_handler)

# and start the bot...
updater.start_polling()
