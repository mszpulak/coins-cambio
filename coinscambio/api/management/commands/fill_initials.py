from django.core.management import BaseCommand
from django.contrib.auth.models import User


class Command(BaseCommand):
    def handle(self, *args, **kwargs):

        for i in range(1000):
            User.objects.create_user(f'user{i}', None, f'user{i}')

