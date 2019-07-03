from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, CallbackQueryHandler, Filters
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

# Initialize bot collection for dividing it by chats
bot_collection = {}

# Initialize buttons for choosing language and theme:
lang_buttons = [[InlineKeyboardButton("Русский", callback_data='RU'),
                InlineKeyboardButton("English", callback_data='EN')]]

theme_buttons_RU = [[InlineKeyboardButton("Города", callback_data='cities'),
                    InlineKeyboardButton("Животные", callback_data='animals')]]

theme_buttons_EN = [[InlineKeyboardButton("Cities", callback_data='cities'),
                    InlineKeyboardButton("Animals", callback_data='animals')]]



# start or restart bot - define attributes or clean them
def start_bot(chat_id, lang):
    if chat_id in bot_collection:
        bot_collection[chat_id].restart_bot(lang)
    else:
        new_bot = WordsGameBot(lang)
        bot_collection[chat_id] = new_bot


# define reaction to /start command in tlgr
def start_callback(bot, update):
    reply_markup = InlineKeyboardMarkup(lang_buttons)
    update.message.reply_text("Выбери язык | Choose language", reply_markup=reply_markup)
    

# Define theme using buttons
def define_bot(bot, update):
    query = update.callback_query
    chat_id = query.message.chat_id
    if query.data in ['RU', 'EN']:
        start_bot(chat_id, query.data)
        reply_markup = (InlineKeyboardMarkup(theme_buttons_EN) if query.data == 'EN' else
                        InlineKeyboardMarkup(theme_buttons_RU))

        bot.edit_message_text(text=bot_collection[chat_id].phrases.first_input, reply_markup=reply_markup,
                              chat_id=query.message.chat_id, message_id=query.message.message_id)
    else:
        bot_collection[chat_id].init_dictionary(query.data)
        bot.edit_message_text(text=bot_collection[chat_id].phrases.give_description(),
                              chat_id=query.message.chat_id, message_id=query.message.message_id)


# define answer to person input
def answer(bot, update):
    user_id = update.message.from_user.id
    if user_id not in bot_collection:
        start_callback(bot, update)
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
define_bot_handler = CallbackQueryHandler(define_bot)

# adding handlers to our dispatcher
dispatcher.add_handler(start_handler)
dispatcher.add_handler(answer_handler)
dispatcher.add_handler(define_bot_handler)

# and start the bot...
updater.start_polling()
