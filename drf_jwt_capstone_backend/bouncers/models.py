from django.db import models

# Create your models here.


class Bouncer(models.Model):
    Name = models.CharField(max_length=50, blank=True)
    Price = models.DecimalField(max_digits=10, decimal_places=2)
    Dimensions = models.TextField(max_length=20)
    Description = models.TextField(max_length=300)