import uuid
from django.db import models
from django.db.models import Sum
from django.conf import settings
from products.models import Product

# Create your models here.


class Order(models.Model):
    order_no = models.CharField(max_length=32, null=False, editable=False)
    name = models.CharField(max_length=50, null=False, blank=False)
    email = models.CharField(max_length=50, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    country = models.CharField(max_length=50, null=False, blank=False)
    county = models.CharField(max_length=50, null=True, blank=True)
    city = models.CharField(max_length=50, null=False, blank=False)
    address_1 = models.CharField(max_length=50, null=False, blank=False)
    address_2 = models.CharField(max_length=50, null=False, blank=False)
    postcode = models.CharField(max_length=50, null=True, blank=True)
    delivery_amount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=False, default=0
        )
    order_amount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=False, default=0
        )
    grand_total = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=False, default=0
        )
    date = models.DateTimeField(auto_now_add=True)

    def _generate_order_number(self):
        return uuid.uuid4().hex.upper() 
    
    def save(self, *args, **kwargs):
        if not self.order_no:
            self.order_no = self._generate_order_number()
        super().save(*args, **kwargs)

    def update_total(self):
        self.order_amount = self.lineitems.aggregate(Sum('lineitem_total'))['lineitem_total__sum']
        if self.order_amount < settings.FREE_DELIVERY_THRESHOLD:
            self.delivery_amount = self.order_amount * settings.STANDARD_DELIVERY_PERCENTAGE / 100
        else:
            self.delivery_amount = 0
        self.grand_total = self.order_amount + self.delivery_amount
        self.save()
    
    def __str__(self):
        return f'{self.order_no} - {self.name}'


class OrderLineItem(models.Model):
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        related_name='lineitems'
        )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        null=False,
        blank=False
        )
    product_size = models.CharField(max_length=2, null=True, blank=True)
    quantity = models.IntegerField(null=False, blank=False, default=0)
    lineitem_total = models.DecimalField(
        decimal_places=2,
        max_digits=6,
        null=False,
        blank=False,
        editable=False
        )
    
    def save(self, *args, **kwargs):
        self.lineitem_total = self.product.price * self.quantity
        super().save(*args, **kwargs)

