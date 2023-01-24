from django.db import models

# Create your models here.

class Shop_item(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    net_weight = models.CharField(max_length=50)
    flavour = models.CharField(max_length=50)
    def __str__(self):
        return self.name + ', ' + self.flavour 

class Cart_item(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    net_weight = models.CharField(max_length=50)
    flavour = models.CharField(max_length=50)
    def __str__(self):
        return self.name + ', ' + self.flavour

