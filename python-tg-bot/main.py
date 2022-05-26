import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CallbackContext, CommandHandler

from config.runConfig import config

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
from telegram.ext import CommandHandler



if __name__ == '__main__':
    application = ApplicationBuilder().token(config.bot_token).build()

    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)

    application.run_polling()