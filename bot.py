from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    ContextTypes,
)
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Welcome to Rajasthan Medical Officer Quiz Bot!\n\n"
        "Daily Quiz jaldi shuru honge.\n"
        "Admin setup complete hone ke baad bot automatically questions bhejega."
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "/start - Bot Start\n"
        "/help - Help\n"
        "/today - Today's Quiz (Coming Soon)"
    )

app = ApplicationBuilder().token(BOT_TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("help", help_command))

print("Bot Started...")

app.run_polling()
