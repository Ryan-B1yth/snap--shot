from django.contrib import admin
from django.urls import path, include
from .views import basket

urlpatterns = [
    path('', basket, name='basket')
]