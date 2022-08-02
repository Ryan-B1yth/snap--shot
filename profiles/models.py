""" Import s"""
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from django_countries.fields import CountryField


class Profile(models.Model):
    """ Profile model """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    default_phone_number = models.CharField(
        max_length=20, null=True, blank=True
        )
    default_country = CountryField(
        blank_label="Country", null=True, blank=True
        )
    default_county = models.CharField(max_length=50, null=True, blank=True)
    default_city = models.CharField(max_length=50, null=True, blank=True)
    default_address_1 = models.CharField(max_length=50, null=True, blank=True)
    default_address_2 = models.CharField(max_length=50, null=True, blank=True)
    default_postcode = models.CharField(max_length=50, null=True, blank=True)


@receiver(post_save, sender=User)
def create_or_update_profile(sender, instance, created, **kwargs):
    """ Create or update user profile """
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()
