from django.urls import path
from .views import checkout, checkout_success, cache_checkout_data
from .webhooks import webhook

urlpatterns = [
    path('', checkout, name='checkout'),
    path('success/<order_no>', checkout_success, name='checkout_success'),
    path('wh/', webhook, name='webhook'),
    path('cache/', cache_checkout_data, name='cache'),
]
