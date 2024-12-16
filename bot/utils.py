
import requests
from django.http import JsonResponse
from django.conf import settings

def set_telegram_webhook(request):
    TELEGRAM_TOKEN = settings.TELEGRAM_TOKEN  # Set your token in settings.py
    TELEGRAM_URL = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/setWebhook"

    # Your webhook URL on Render
    webhook_url = "https://telebot-p95r.onrender.com/bot/telegram-webhook/"

    # Send the POST request to set the webhook
    response = requests.post(TELEGRAM_URL, data={"url": webhook_url})

    # Return the response from Telegram API
    if response.status_code == 200:
        return JsonResponse({"status": "success", "message": "Webhook set successfully."})
    else:
        return JsonResponse({"status": "error", "message": "Failed to set webhook."})
