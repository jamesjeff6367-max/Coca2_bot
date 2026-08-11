import os
import logging
from dotenv import load_dotenv
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CommandHandler, ContextTypes

load_dotenv()

logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)
logger = logging.getLogger(__name__)

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHANNEL_LINK = os.getenv("CHANNEL_LINK")
REGISTER_LINK = os.getenv("REGISTER_LINK")
SUPPORT_USERNAME = os.getenv("SUPPORT_USERNAME")
# Add a new env variable for the image URL (optional but recommended)
IMAGE_URL = os.getenv("IMAGE_URL", "https://i.imgur.com/your-image.jpg")   # <-- change to your actual URL

if not all([BOT_TOKEN, CHANNEL_LINK, REGISTER_LINK, SUPPORT_USERNAME]):
    raise ValueError("Missing environment variables. Check your .env file.")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a welcome photo with caption and inline buttons."""
    keyboard = [
        [InlineKeyboardButton("📢 Join Channel", url=CHANNEL_LINK)],
        [InlineKeyboardButton("🔗 Register Now", url=REGISTER_LINK)],
        [InlineKeyboardButton("💬 Contact Support", url=f"https://t.me/{SUPPORT_USERNAME}")],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    caption = (
        "👋 Welcome to Paisa Base!\n\n"
        "🚀 Maximize your earnings with us.\n"
        "• 4.5% on INR\n"
        "• USDT108 fast sales\n"
        "• 24/7 customer care\n\n"
        "Join our channel, register, or contact support using the buttons below."
    )

    # Send the photo with caption and buttons
    await update.message.reply_photo(
        photo=IMAGE_URL,           # URL or local file path (e.g., "welcome.png")
        caption=caption,
        reply_markup=reply_markup
    )

def main():
    application = Application.builder().token(BOT_TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.run_polling()

if __name__ == "__main__":
    main()
