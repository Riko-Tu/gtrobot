from telegram import Update
from telegram.ext import filters, MessageHandler, ApplicationBuilder, CommandHandler, CallbackContext

from config.runConfig import config

...

#恢复所有收到的消息
async def echo(update: Update, context: CallbackContext.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)

async def caps(update: Update, context: CallbackContext):
    text_caps = ' '.join(context.args).upper()
    await context.bot.send_message(chat_id=update.effective_chat.id, text=text_caps)

##收到/start后回话
async def start(update: Update, context: CallbackContext.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")


if __name__ == '__main__':
    #获取程序对象
    application = ApplicationBuilder().token(config.bot_token).build()
    #回声
    echo_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), echo)

    caps_handler = CommandHandler('caps', caps)

    #/start
    start_handler = CommandHandler('start', start)

    #添加功能
    application.add_handler(start_handler)
    application.add_handler(echo_handler)
    application.add_handler(caps_handler)

    #启动
    application.run_polling()