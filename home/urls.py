from django.urls import path
from . import views

# Home URLS
urlpatterns = [
    path('', views.index, name='home'),
]
