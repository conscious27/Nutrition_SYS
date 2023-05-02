from django.urls import path
from recipe_management import views

urlpatterns = [
    path('generate_recommendations', views.generate_recommendation, name='generate_recommendation'),
    path('recipe/<str:recipe_name>/', views.display_recipe, name='display_recipe'),
    path('like_meal/<int:id>/<str:type>/', views.like_meal, name='like-meal'),
    path('dislike_meal/<int:id>/<str:type>/', views.dislike_meal, name='dislike_meal')
]