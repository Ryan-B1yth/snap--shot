from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    default_phone_number = models.CharField(max_length=20, null=True, blank=True)
    default_country = CountryField(blank_label="Country", null=True, blank=True)
    default_county = models.CharField(max_length=50, null=True, blank=True)
    default_city = models.CharField(max_length=50, null=True, blank=True)
    default_address_1 = models.CharField(max_length=50, null=True, blank=True)
    default_address_2 = models.CharField(max_length=50, null=True, blank=True)
    default_postcode = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.user.name

@receiver(post_save, sender=User)
def create_or_update_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()
