from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    CallbackContext,
)
from bot.utils import convert_crypto
import os

# Replace with your CoinMarketCap API Key
COINMARKETCAP_API_KEY =os.environ.get('CRYPTO_API_KEY')

async def start(update: Update, context: CallbackContext):
    await update.message.reply_text("Welcome to Crypto Converter Bot! Use /convert to get started.")

async def convert(update: Update, context: CallbackContext):
    try:
        args = context.args  # Parse user input
        if len(args) != 3:
            await update.message.reply_text("Usage: /convert <amount> <from_currency> <to_currency>")
            return

        amount = float(args[0])
        from_currency = args[1].upper()
        to_currency = args[2].upper()

        price = convert_crypto(amount, from_currency, to_currency, COINMARKETCAP_API_KEY)
        if price is not None:
            await update.message.reply_text(f"{amount} {from_currency} = {price:.2f} {to_currency}")
        else:
            await update.message.reply_text("Error converting currencies. Please try again later.")
    except Exception as e:
        await update.message.reply_text(f"An error occurred: {e}")

def main():
    # Replace with your Telegram Bot Token
    TELEGRAM_TOKEN =os.environ.get('TELEGRAM_TOKEN')
    
    # Create the application object
    application = Application.builder().token(TELEGRAM_TOKEN).build()

    # Add command handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("convert", convert))

    # Start the bot
    application.run_polling()
