
# urls.py
from django.urls import path
from .views import telegram_webhook
from . import views

urlpatterns = [
    path("telegram-webhook/", telegram_webhook, name="telegram_webhook"),
    path('', views.set_telegram_webhook, name='webhook'),
]
