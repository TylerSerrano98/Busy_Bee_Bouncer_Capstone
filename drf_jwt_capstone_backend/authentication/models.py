from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

# To add new columns to the authentication_user table include the properties
# in the model below
# In order for the new columns to appear in the database run:
# 1. python manage.py makemigrations
# 2. python manage.py migrate


class User(AbstractUser):
    Middle_Name = models.CharField(max_length=20)
    Home_Address = models.TextField(max_length=100, default='default')
    Phone_Number = models.TextField(max_length=12, default='default')

