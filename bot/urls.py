
# urls.py
from django.urls import path
from .views import telegram_webhook

urlpatterns = [
    path("telegram-webhook/", telegram_webhook, name="telegram_webhook"),
]
