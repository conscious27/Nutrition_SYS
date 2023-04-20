from django.contrib import admin
from django.urls import path
from user_management import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create_user_profile', views.create_user_profile, name='create_user_profile')
]
