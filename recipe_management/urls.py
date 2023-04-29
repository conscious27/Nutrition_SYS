from django.urls import path, include
from recipe_management import views

urlpatterns = [
    path('generate_recommendations', views.generate_recommendation, name='generate_recommendation'),
    path('recipe/<str:recipe_name>/', views.display_recipe, name='display_recipe')
]