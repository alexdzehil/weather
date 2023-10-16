from django.core.management.base import BaseCommand

from apps.tg_bot.views import main


class Command(BaseCommand):
    help = 'Implemented to Django application telegram bot setup command'

    def handle(self, *args, **kwargs):
        main()
