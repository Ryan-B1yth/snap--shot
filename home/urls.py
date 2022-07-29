""" Imports """
from django.urls import path
from .views import index, create_testimony

urlpatterns = [
    path('', index, name="home"),
    path('testimonies/', create_testimony, name="testimony")
]
