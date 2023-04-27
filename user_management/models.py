from django.db import models
from django.contrib.auth.models import User
# Create your models here.

# from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# class CustomUserManager(BaseUserManager):
#     def create_user(self, email, password=None, **extra_fields):
#         if not email:
#             raise ValueError('The Email field must be set')
#         email = self.normalize_email(email)
#         user = self.model(email=email, **extra_fields)
#         user.set_password(password)
#         user.save(using=self._db)
#         return user

#     def create_superuser(self, email, password=None, **extra_fields):
#         extra_fields.setdefault('is_staff', True)
#         extra_fields.setdefault('is_superuser', True)
#         return self.create_user(email, password, **extra_fields)

# class User(AbstractBaseUser):
#     email = models.EmailField(unique=True)
#     first_name = models.CharField(max_length=30)
#     last_name = models.CharField(max_length=30)
#     date_of_birth = models.DateField(null=True, blank=True)
#     is_active = models.BooleanField(default=True)
#     is_staff = models.BooleanField(default=False)

#     objects = CustomUserManager()

#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['first_name', 'last_name']

#     def __str__(self):
#         return self.email

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
    physical_activity = models.DecimalField(max_digits=6,decimal_places=1, choices=PHYSICAL_ACTIVITY_CHOICES)
    RESTRICTIONS = (
        ('Egg', 'Egg'),
        ('Red Meat', 'Red Meat'), 
        ('Fish', 'Fish'), 
        ('Milk', 'Milk'),
        ('None', 'None')
    )
    dietary_restriction = models.CharField(max_length=10, choices= RESTRICTIONS)
