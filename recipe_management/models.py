from django.db import models

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