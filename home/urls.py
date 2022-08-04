""" Imports """
from django.urls import path
from .views import index, create_testimony, privacy_policy

urlpatterns = [
    path('', index, name="home"),
    path('testimonies/', create_testimony, name="testimony"),
    path('privacy/', privacy_policy, name="privacy"),
]
