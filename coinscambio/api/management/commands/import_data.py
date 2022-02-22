import sys

from django.core.management import BaseCommand
import os
import csv
from django.contrib.auth.models import User
from api.models import Coins


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('filename', type=str)

    def handle(self, *args, **options):
        User.objects.all().delete()
        filename = options['filename']
        self.stdout.write(os.path.dirname(os.path.abspath(__file__)))
        filename = os.path.join(os.path.dirname(os.path.abspath(__file__)), filename)
        with open(filename, newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            next(reader)
            for row in reader:
                username, first_name, last_name, email, referee, coins = row
                self.stdout.write(f"processing user {username} {first_name} {last_name}")
                u = User.objects.create_user(username=username,
                                         first_name=first_name,
                                         last_name=last_name,
                                         email=email,
                                         )
                Coins.objects.create(user=u, value=int(coins))
                if referee:
                    u.coins.value += 20
                u.save()

