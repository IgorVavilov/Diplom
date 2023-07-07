from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

from .views import *

urlpatterns = [
    path('', views.profiles, name='profiles'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('profile_form/', views.edit_account, name='profile_form'),
    path('account/', views.user_account, name='account'),

    path('contact/', views.contact, name='contact'),
    path('inbox/', views.inbox, name='inbox'),
    path('message/<str:pk>', views.view_message, name='message'),
]