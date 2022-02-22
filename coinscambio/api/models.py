from django.contrib.auth.models import User
from django.db import models


class Coins(models.Model):
    value = models.IntegerField(default=0)
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
