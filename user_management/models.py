from django.db import models

# Create your models here.

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)

class User(AbstractBaseUser):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    date_of_birth = models.DateField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def __str__(self):
        return self.email


class Profile(models.Model):
    user  = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.IntegerField(null=True, blank=True)
    weight = models.FloatField()
    height = models.FloatField()
    DIABETES_CHOICES = (
        ('Type 1', 'Type 1'),
        ('Type 2', 'Type 2')
    )
    diabetes = models.CharField(max_length=6, choices=DIABETES_CHOICES, null=True, blank=True)
    blood_glucose_level = models.DecimalField(max_digits=6, decimal_places=2)
    blood_pressure = models.DecimalField(max_digits=6, decimal_places=2)
    physical_activity_daily = models.DecimalField(max_digits=6, decimal_places=2)
    RESTRICTIONS = (
        ('Egg', 'Egg'),
        ('Red Meat', 'Red Meat'), 
        ('Fish', 'Fish'), 
        ('Milk', 'Milk')
    )
    dietary_restriction = models.CharField(max_length=10, choices= RESTRICTIONS, null=True, blank=True)
