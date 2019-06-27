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
list_of_bots = {}

# Initialize updater and dispatcher... as like I know what it is
updater = Updater(token=TLGR_TOKEN)
dispatcher = updater.dispatcher

# user = telegram.user
# print(user)
bot_collection = {}
my_bot = WordsGameBot('data/citiesForTest.txt')

# def start_bot(user_id):
#     if user_id in bot_collection.keys():
#         bot_collection.values(user_id) = WordsGameBot('data/citiesForTest.txt')
#     else:
#         bot_collection.
# #     Найти бота по user_id, заново его инициализировать
# #     Если  по user_id ни кого не нашли - вносим заново
# #     Я пока вижу единственный вариант с глобальной переменной bot_collection
# #     Не понимаю, как напрямую передавать его из callback (мы ж ее без параметров вызыываем...)

# define reaction to /start command in tlgr
def start_callback(bot, update):
    # start_bot(update.message.from_user.id)
    update.message.reply_text(my_bot.phrases.give_description())

def restart_callback(bot, update):
    # start_bot(update.message.from_user.id)
    update.message.reply_text(my_bot.phrases.restart_phrases())

# define reaction to person input
def answer(bot, update):
    bot_answer = my_bot.bot_answer_is(update.message.text.strip())
    bot.send_message(chat_id=update.message.chat_id, text=bot_answer)


# define all handlers
answer_handler = MessageHandler(Filters.text, answer)
start_handler = CommandHandler("start", start_callback)
restart_handler = CommandHandler('restart', restart_callback)

# adding handlers to our dipatcher
dispatcher.add_handler(start_handler)
dispatcher.add_handler(answer_handler)
dispatcher.add_handler(restart_handler)

# and start the bot...
updater.start_polling()
