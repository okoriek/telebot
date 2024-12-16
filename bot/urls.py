
# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path("telegram-webhook/", views.telegram_webhook, name="telegram_webhook"),
    path('', views.set_telegram_webhook, name='webhook'),
]
