from django.contrib import admin
from django.urls import path, include
from .views import basket_view, add_to_basket

urlpatterns = [
    path('', basket_view, name='basket'),
    path('add/<product_id>/', add_to_basket, name='add_to_basket')
]