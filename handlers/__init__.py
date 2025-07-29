from telegram.ext import Application, CommandHandler
from handlers.start import start
from handlers.other_handlers import *

def register_handlers(application: Application):
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help))
    application.add_handler(CommandHandler("about", about))
    application.add_handler(CommandHandler("add", add))
    application.add_handler(CommandHandler("list", list_entries))
