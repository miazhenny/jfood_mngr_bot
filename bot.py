from telegram import Update
from telegram.ext import Application, CommandHandler
from dotenv import load_dotenv
import os
from handlers.start import start
from handlers.other_handlers import help
from handlers import register_handlers
load_dotenv()


def main():
    bot_token = os.getenv("BOT_TOKEN")
    if not bot_token:
        raise ValueError("BOT_TOKEN environment variable is not set.")
    application = Application.builder().token(bot_token).build()
    register_handlers(application)
    application.run_polling()
    

if __name__ == "__main__":
    main()