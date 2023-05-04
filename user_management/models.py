from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    user  = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.IntegerField(null=True, blank=True)
    height = models.DecimalField(max_digits=6, decimal_places=2)
    weight = models.DecimalField(max_digits=6, decimal_places=2)
    cholesterol_level = models.DecimalField(max_digits=6, decimal_places=2)
    glucose_level = models.DecimalField(max_digits=6, decimal_places=2)
    blood_pressure = models.DecimalField(max_digits=6, decimal_places=2)
    PHYSICAL_ACTIVITY_CHOICES = (
        (1.4, 'sedentary_lifestyle'),
        (1.6, 'low_active_lifestyle'),
        (1.8, 'moderate_lifestyle'),
        (2.0, 'active_lifestyle'),
        (2.2, 'very_active_lifestyle')
    )
    physical_activity = models.FloatField(choices=PHYSICAL_ACTIVITY_CHOICES)
    RESTRICTIONS = (
        ('Egg', 'Egg'),
        ('Red Meat', 'Red Meat'), 
        ('Fish', 'Fish'), 
        ('Milk', 'Milk'),
        ('None', 'None')
    )
    dietary_restriction = models.CharField(max_length=10, choices= RESTRICTIONS)
