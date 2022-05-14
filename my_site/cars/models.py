from email.policy import default
from statistics import mode
from django.db import models

# Create your models here.
class Cars(models.Model):
    brand = models.CharField(max_length=30)
    year = models.IntegerField()