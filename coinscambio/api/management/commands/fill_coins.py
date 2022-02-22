from django.core.management import BaseCommand
from django.contrib.auth.models import User
from api.models import Coins
import random


class Command(BaseCommand):
    def handle(self, *args, **kwargs):

        for u in User.objects.all():
            c = Coins(user=u, value=random.randint(0,100))
            c.save()
