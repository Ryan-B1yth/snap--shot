""" Imports """
from django.urls import path
from .views import basket_view, add_to_basket, update_basket, remove_item

urlpatterns = [
    path('', basket_view, name='basket'),
    path('add/<product_id>/', add_to_basket, name='add_to_basket'),
    path('update/<product_id>/', update_basket, name='update_basket'),
    path('remove/<product_id>/', remove_item, name='remove_item'),
]
