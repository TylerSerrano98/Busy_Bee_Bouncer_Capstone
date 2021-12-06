from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()
# Create your models here.


class Bouncer(models.Model):
    User = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    Items = models.TextField(max_length=50, blank=True)
    Price = models.DecimalField(max_digits=10, decimal_places=2)
    Dimensions = models.TextField(max_length=20)
    Description = models.TextField(max_length=300)