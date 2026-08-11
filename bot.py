import os
import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Setup Inline Keyboard Buttons with your custom links
    keyboard = [
        [
            InlineKeyboardButton(
                "📈 Register on Paisa Base", 
                url="https://wallet.paisa-base.com/register?inviteCode=phar6p"
            )
        ],
        [
            InlineKeyboardButton(
                "📢 Join Official Channel", 
                url="https://t.me/+oTUFYl-kubM1OTU1"
            )
        ],
        [
            InlineKeyboardButton(
                "💬 Customer Support", 
                url="https://t.me/jetlee261"
            )
        ]
    ]
    
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    caption_text = (
        "🔥 **MAXIMIZE YOUR EARNINGS WITH PAISA BASE** 🔥\n\n"
        "• 4.5% ON INR | USDT 108\n"
        "• Fast Sales & Set Your Own Limit\n"
        "• 24/7 Customer Care Support\n\n"
        "Click the buttons below to get started!"
    )
    
    # Send local image with buttons
    photo_path = 'image.jpg'
    if os.path.exists(photo_path):
        with open(photo_path, 'rb') as photo:
            await update.message.reply_photo(
                photo=photo,
                caption=caption_text,
                parse_mode='Markdown',
                reply_markup=reply_markup
            )
    else:
        # Fallback text if image file is missing
        await update.message.reply_text(
            text=caption_text,
            parse_mode='Markdown',
            reply_markup=reply_markup
        )

def main():
    # Retrieve Bot Token from Environment Variables
    token = os.environ.get("BOT_TOKEN")
    if not token:
        raise ValueError("No BOT_TOKEN set in environment variables.")

    application = ApplicationBuilder().token(token).build()
    
    # Register /start command
    application.add_handler(CommandHandler("start", start))
    
    # Start polling for Telegram messages
    application.run_polling()

if __name__ == '__main__':
    main()
