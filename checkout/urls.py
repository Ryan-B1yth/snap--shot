from django.urls import path
from .views import checkout, checkout_success

urlpatterns = [
    path('', checkout, name='checkout'),
    path('success/<order_no>', checkout_success, name='checkout_success'),
]
