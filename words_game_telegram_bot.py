import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from dotenv import load_dotenv
import logging
import os
from os.path import join, dirname

import bot_answers

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

# define reaction to /start command in tlgr
def start_callback(bot, update):
    update.message.reply_text(game_language.give_description())

# define reaction to person input
def answer(bot, update):
    bot_answer = whole_game(update.message.text)
    bot.send_message(chat_id=update.message.chat_id, text=bot_answer)


# define all handlers
answer_handler = MessageHandler(Filters.text, answer)
start_handler = CommandHandler("start", start_callback)

# adding handlers to our dipatcher
dispatcher.add_handler(start_handler)
dispatcher.add_handler(answer_handler)

# and start the bot...
updater.start_polling()
