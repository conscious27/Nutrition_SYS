from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class FoodItem(models.Model):
    name = models.CharField(max_length=200)
    groups = models.CharField(max_length=10)
    calories = models.DecimalField(max_digits=6, decimal_places=2)
    total_fat = models.DecimalField(max_digits=5, decimal_places=2)
    saturated_fat = models.DecimalField(max_digits=5, decimal_places=2)
    cholesterol = models.DecimalField(max_digits=6, decimal_places=2)
    protein = models.DecimalField(max_digits=6, decimal_places=2)
    carbohydrates = models.DecimalField(max_digits=6, decimal_places=2)
    fiber = models.DecimalField(max_digits=6, decimal_places=2)
    sugars = models.DecimalField(max_digits=6, decimal_places=2)
    category1 = models.CharField(max_length=20, null=True, blank=True)
    category2 = models.CharField(max_length=20, null=True, blank=True)

class Breakfast_meal(models.Model):
    food1 = models.CharField(max_length=200)
    food2 = models.CharField(max_length=200)
    food3 = models.CharField(max_length=200)
    calories = models.DecimalField(max_digits=6, decimal_places=2)
    total_fat = models.DecimalField(max_digits=5, decimal_places=2)
    cholesterol = models.DecimalField(max_digits=6, decimal_places=2)
    protein = models.DecimalField(max_digits=6, decimal_places=2)
    carbohydrates = models.DecimalField(max_digits=6, decimal_places=2)
    fiber = models.DecimalField(max_digits=6, decimal_places=2)
    sugars = models.DecimalField(max_digits=6, decimal_places=2)

class Lunch_meal(models.Model):
    food1 = models.CharField(max_length=200)
    food2 = models.CharField(max_length=200)
    food3 = models.CharField(max_length=200)
    calories = models.DecimalField(max_digits=6, decimal_places=2)
    total_fat = models.DecimalField(max_digits=5, decimal_places=2)
    cholesterol = models.DecimalField(max_digits=6, decimal_places=2)
    protein = models.DecimalField(max_digits=6, decimal_places=2)
    carbohydrates = models.DecimalField(max_digits=6, decimal_places=2)
    fiber = models.DecimalField(max_digits=6, decimal_places=2)
    sugars = models.DecimalField(max_digits=6, decimal_places=2)

class Dinner_meal(models.Model):
    food1 = models.CharField(max_length=200)
    food2 = models.CharField(max_length=200)
    food3 = models.CharField(max_length=200)
    calories = models.DecimalField(max_digits=6, decimal_places=2)
    total_fat = models.DecimalField(max_digits=5, decimal_places=2)
    cholesterol = models.DecimalField(max_digits=6, decimal_places=2)
    protein = models.DecimalField(max_digits=6, decimal_places=2)
    carbohydrates = models.DecimalField(max_digits=6, decimal_places=2)
    fiber = models.DecimalField(max_digits=6, decimal_places=2)
    sugars = models.DecimalField(max_digits=6, decimal_places=2)


class Day_meal(models.Model):
    breakfast_food1 = models.CharField(max_length=200)
    breakfast_food2 = models.CharField(max_length=200)
    breakfast_food3 = models.CharField(max_length=200)
    lunch_food1 = models.CharField(max_length=200)
    lunch_food2 = models.CharField(max_length=200)
    lunch_food3 = models.CharField(max_length=200)
    dinner_food1 = models.CharField(max_length=200)
    dinner_food2 = models.CharField(max_length=200)
    dinner_food3 = models.CharField(max_length=200)
    total_calories = models.DecimalField(max_digits=6, decimal_places=2)
    total_fat = models.DecimalField(max_digits=5, decimal_places=2)
    total_cholesterol = models.DecimalField(max_digits=6, decimal_places=2)
    total_protein = models.DecimalField(max_digits=6, decimal_places=2)
    total_carbohydrates = models.DecimalField(max_digits=6, decimal_places=2)
    total_fiber = models.DecimalField(max_digits=6, decimal_places=2)
    total_sugars = models.DecimalField(max_digits=6, decimal_places=2)

class BreakfastMealFeedback(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    breakfast_meal = models.ForeignKey(Breakfast_meal, on_delete=models.CASCADE)
    like = models.BooleanField(default=False)
    dislike = models.BooleanField(default=False)

class LunchMealFeedback(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    lunch_meal = models.ForeignKey(Lunch_meal, on_delete=models.CASCADE)
    like = models.BooleanField(default=False)
    dislike = models.BooleanField(default=False)

class DinnerMealFeedback(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    dinner_meal = models.ForeignKey(Dinner_meal, on_delete=models.CASCADE)
    like = models.BooleanField(default=False)
    dislike = models.BooleanField(default=False)
