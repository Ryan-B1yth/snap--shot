from django.urls import path
from .views import user_profile, order_history

urlpatterns = [
    path('', user_profile, name='user_profile'),
    # path('order_history/<order_no>', order_history, name='order_history'),
]
