import os
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Logging setup
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Hello! Bot is up and running.")

def main():
    token = os.getenv("BOT_TOKEN")
    if not token:
        raise ValueError("BOT_TOKEN environment variable not set!")

    application = ApplicationBuilder().token(token).build()
    
    # Register handlers
    application.add_handler(CommandHandler("start", start))
    
    # Start polling
    application.run_polling()

if __name__ == "__main__":
    main()
