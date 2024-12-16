from django.core.management.base import BaseCommand
from bot.bot import main

class Command(BaseCommand):
    help = "Start the Telegram bot"

    def handle(self, *args, **kwargs):
        self.stdout.write("Starting Telegram bot...")
        main()
