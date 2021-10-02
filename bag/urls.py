from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_bag, name='view_bag'),
    path('add/<item_id>/', views.add_to_order, name='add_to_order'),
    path('update/<item_id>/', views.update_order, name='update_order'),
]
