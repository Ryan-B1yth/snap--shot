""" Imports """
from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    """ Categories model """
    name = models.CharField(max_length=100)
    friendly_name = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return str(self.friendly_name)

    def get_friendly_name(self):
        return self.friendly_name

    class Meta:
        verbose_name_plural = 'Categories'


class Product(models.Model):
    """ Product model """
    category = models.ForeignKey(
        Category,
        null=True,
        blank=True,
        on_delete=models.SET_NULL
        )
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(
        max_digits=3,
        decimal_places=1,
        null=True,
        blank=True
        )
    image = models.ImageField(null=True, blank=True)
    sizes = models.BooleanField(default=False, null=True, blank=True)

    def __str__(self):
        return str(self.name)


class Review(models.Model):
    """ Product review """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(max_length=250, null=False, blank=False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
