from django.contrib import admin
from django.urls import path, include
from .views import all_products, product_detail, add_product

urlpatterns = [
    path('', all_products, name='products'),
    path('<int:product_id>/', product_detail, name='product_detail'),
    path('add/', add_product, name='add_product'),
]
