import os
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Enable logging so you can see errors in Railway logs
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# /start command handler
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Hello! Your bot is working correctly now.")

def main():
    # Fetch token from Environment Variables in Railway
    token = os.getenv("BOT_TOKEN")
    
    if not token:
        print("ERROR: BOT_TOKEN environment variable is missing!")
        return

    # Build the application
    application = ApplicationBuilder().token(token).build()

    # Add handlers
    application.add_handler(CommandHandler("start", start))

    # Run the bot
    print("Bot is starting...")
    application.run_polling()

if __name__ == "__main__":
    main()
