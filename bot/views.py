import requests
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

import os

TELEGRAM_TOKEN = os.environ.get('TELEGRAM_TOKEN')
TELEGRAM_URL = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}"

# CoinMarketCap API details
COINMARKETCAP_API_KEY = os.environ.get('CRYPTO_API_KEY')
COINMARKETCAP_API_URL = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest"

@csrf_exempt
def telegram_webhook(request):
    if request.method == "POST":
        data = json.loads(request.body)
        chat_id = data.get("message", {}).get("chat", {}).get("id")
        text = data.get("message", {}).get("text")

        if chat_id and text:
            # Process the "/convert" command
            if text.startswith("/convert"):
                # Example: "/convert 1 BTC to USD"
                parts = text.split()
                if len(parts) == 5:
                    amount = parts[1]
                    from_currency = parts[2].upper()
                    to_currency = parts[4].upper()

                    result = convert_currency(amount, from_currency, to_currency)
                    send_message(chat_id, result)
                else:
                    send_message(chat_id, "Invalid command format. Use: /convert <amount> <from_currency> to <to_currency>")
            else:
                send_message(chat_id, "Send /convert <amount> <from_currency> to <to_currency> to convert cryptocurrencies.")
        return JsonResponse({"status": "ok"}, status=200)
    return JsonResponse({"error": "Invalid method"}, status=405)

def send_message(chat_id, text):
    """Send a message to the Telegram user."""
    url = f"{TELEGRAM_URL}/sendMessage"
    payload = {"chat_id": chat_id, "text": text}
    requests.post(url, json=payload)

def convert_currency(amount, from_currency, to_currency):
    """Convert currency using the CoinMarketCap API."""
    headers = {
        'X-CMC_PRO_API_KEY': COINMARKETCAP_API_KEY,
        'Accept': 'application/json',
    }
    params = {
        'symbol': from_currency,
        'convert': to_currency
    }

    try:
        response = requests.get(COINMARKETCAP_API_URL, headers=headers, params=params)
        data = response.json()

        if 'data' in data and from_currency in data['data']:
            price = data['data'][from_currency]['quote'][to_currency]['price']
            converted_amount = float(amount) * price
            return f"{amount} {from_currency} is {converted_amount:.2f} {to_currency}"
        else:
            return f"Conversion between {from_currency} and {to_currency} is not available."
    except Exception as e:
        return f"Error: {str(e)}"
