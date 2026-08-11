import os
import logging
from dotenv import load_dotenv
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CommandHandler, ContextTypes

# Load the .env file (only for local testing)
load_dotenv()

# Set up logging so we can see errors
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

# Read all the variables from the .env file
BOT_TOKEN = os.getenv("BOT_TOKEN")
CHANNEL_LINK = os.getenv("CHANNEL_LINK")
REGISTER_LINK = os.getenv("REGISTER_LINK")
SUPPORT_USERNAME = os.getenv("SUPPORT_USERNAME")
IMAGE_URL = os.getenv("IMAGE_URL")

# Check if any variable is missing
if not all([BOT_TOKEN, CHANNEL_LINK, REGISTER_LINK, SUPPORT_USERNAME, IMAGE_URL]):
    raise ValueError("Missing environment variables. Check your .env file.")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """This function runs when someone sends /start"""
    
    # Create the 3 buttons
    keyboard = [
        [InlineKeyboardButton("📢 Join Channel", url=CHANNEL_LINK)],
        [InlineKeyboardButton("🔗 Register Now", url=REGISTER_LINK)],
        [InlineKeyboardButton("💬 Contact Support", url=f"https://t.me/{SUPPORT_USERNAME}")],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    # The text that will appear below the image
    caption = (
        "👋 Welcome to Paisa Base!\n\n"
        "🚀 Maximize your earnings with us.\n"
        "• 4.5% on INR\n"
        "• USDT108 fast sales\n"
        "• 24/7 customer care\n\n"
        "Join our channel, register, or contact support using the buttons below."
    )

    # Send the image + caption + buttons all together
    await update.message.reply_photo(
        photo=IMAGE_URL,
        caption=caption,
        reply_markup=reply_markup
    )

def main():
    """Start the bot"""
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    print("Bot is running... Press Ctrl+C to stop.")
    app.run_polling()

if __name__ == "__main__":
    main()
