from telegram import Update
from telegram.ext import ContextTypes
from services.database import add_jfood_entry, list_jfood_entries

async def help(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if update.message is not None:
        await update.message.reply_text(
            "Available commands:\n"
            "/start - Start the bot\n"
            "/help - Show this help message"
    )
    else:
        pass

async def about(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if update.message is not None:
        await update.message.reply_text(
            "Jfood_manager bot v1.0\nCreated to help you to lvlup your jfood tenacity through managing consumption rate and volume!"
        )
    else:
        pass
    # If the message is None, we do not send a reply
    # This can happen if the update is not a message update
    # or if the message is edited, etc.
    return

async def add(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if update.message is not None:
        entry = " ".join(context.args) if context.args else "(no entry provided)"
        add_jfood_entry(entry)
        await update.message.reply_text(f"Added food entry: {entry}")

async def list_entries(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if update.message is not None:
        entries = list_jfood_entries()
        if entries:
            await update.message.reply_text("Food entries: \n" + "\n".join(entries))
        else:
            await update.message.reply_text("No food entries yet")