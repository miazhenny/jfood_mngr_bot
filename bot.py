from telegram import Update
from telegram.ext import Application, CommandHandler, CallbackContext, ContextTypes, Updater
from dotenv import load_dotenv

import os

load_dotenv()


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if update.message is not None:
        await update.message.reply_text('Hello! I am your bot, ready to assist you.')

def main():
    bot_token = os.getenv("BOT_TOKEN")
    if not bot_token:
        raise ValueError("BOT_TOKEN environment variable is not set.")
    application = Application.builder().token(bot_token).build()
    application.add_handler(CommandHandler("start", start))
    application.run_polling()

if __name__ == "__main__":
    main()