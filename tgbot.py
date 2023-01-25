import logging
import telegram.ext

from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, filters, MessageHandler, InlineQueryHandler
from os import getenv

BOT_TOKEN = getenv("BOT_TOKEN")
API_ID = getenv("API_ID")
API_HASH = getenv("API_HASH")
COMMAND_PREFIXES = getenv("COMMAND_PREFIXES", "#")

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

updater = telegram.ext.Updater("BOT_TOKEN", update_queue=True)

application = ApplicationBuilder

async def alewaah(update: Update, context: ContextTypes.DEFAULT_TYPE):
      await context.bot.send_message(chat_id=update.effective_chat.id, text="Alewaaaah 😂😂")

async def awesome(update: Update, context: ContextTypes.DEFAULT_TYPE):
      await context.bot.send_message(chat_id=update.effective_chat.id, text="I am awesome 😎✌️")

async def cool(update: Update, context: ContextTypes.DEFAULT_TYPE):
      await context.bot.send_message(chat_id=update.effective_chat.id, text="Doraemon is always cool")
      
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="I'm alive")

async def song(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="https://youtu.be/UtF6Jej8yb4")
   
async def nope(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Nope nothing")
    
async def nothing(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Nothing is here🥲😂")
   
if __name__ == '__main__':
        application = ApplicationBuilder().token('5604913977:AAGKzut9MfO8sU17WNo3aXRTlESgmiuzz8k').build()
    
start_handler = CommandHandler('start', start,)
application.add_handler(start_handler)

song_handler = CommandHandler('song', song,)
application.add_handler(song_handler)

alewaah_handler = CommandHandler('alewaah', alewaah)
application.add_handler(alewaah_handler)

awesome_handler = CommandHandler('awesome', awesome,)
application.add_handler(awesome_handler)

cool_handler = CommandHandler('cool', cool,)
application.add_handler(cool_handler)

nope_handler = CommandHandler('nope', nope)
application.add_handler(nope_handler)

nothing_handler = CommandHandler('nothing', nothing,)
application.add_handler(nothing_handler)
    
application.run_polling()

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)

    
if __name__ == '__main__':
    ...
    echo_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), echo)
    
    application.add_handler(start_handler)
    application.add_handler(echo_handler)

    application.run_polling()
    
