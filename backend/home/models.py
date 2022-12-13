from django.conf import settings
from django.db import models
class Product(models.Model):
    'Generated Model'
    name = models.CharField(max_length=100,)
    description = models.TextField()
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10,decimal_places=2,)
    discount = models.DecimalField(max_digits=10,decimal_places=2,)
    hello = models.BinaryField(null=True,blank=True,)
class NewModel1(models.Model):
    'Generated Model'
    stuff = models.CharField(max_length=256,)
