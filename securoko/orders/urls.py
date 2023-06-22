from django.urls import path
from . import views


urlpatterns = [
    path('checkout/', views.order_create, name='order_create'),
    path('profile_orders/<str:pk>/', views.profile_orders, name='profile_orders')
]