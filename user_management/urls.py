from django.contrib import admin
from django.urls import path
from user_management import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup_views', views.signup_views, name='signup_views'),
    path('login_views', views.login_views, name='login_view'),
    path('logout_views', views.logout_views, name='logout_view'),
    path('create_user_profile', views.create_user_profile, name='create_user_profile')
]
