from django.urls import path
from . import views

# Profile view URLS
urlpatterns = [
    path('', views.profile, name='profile'),
    path('order_history/<order_number>',
         views.order_history, name='order_history'),
    path('artwork/<order_id>', views.artwork, name='artwork'),
]
