from os import curdir
from django.core.management.base import BaseCommand
from listing import scheduler as s
from datetime import date, datetime, timedelta
import time

class Command(BaseCommand):
    help = 'Create the json file'

    def handle(self, *args, **kwargs):
        def is_weekend(d = datetime.today().weekday()):
            return d > 4
        
        def market_time():
            now = datetime.now()
            open = now.replace(hour=9, minute=30, second=0)
            close = now.replace(hour=15, minute=30, second=0)
            if now > open and now < close: return True
            return False

        while True:
            if not is_weekend() or not market_time():
                s.metadata_json()
                time.sleep(60)