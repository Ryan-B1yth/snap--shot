from django.db import models
from django.contrib.auth.models import User


class Testimony(models.Model):
    """ Testimony model """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    body = models.TextField(max_length=500, null=False, blank=False)

    def __str__(self):
        return f'{self.user}: {self.body}'
