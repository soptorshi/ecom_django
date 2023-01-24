from django.db import models
# Create your models here.

class Contact(models.Model):
    name = models.CharField( max_length=50)
    email = models.CharField( max_length=70)
    phone = models.CharField( max_length=50)
    desc = models.TextField()
    def __str__(self):
        return self.name + ', ' + self.desc

class Icecream(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    net_weight = models.CharField(max_length=50)
    flavour = models.CharField(max_length=50)
    def __str__(self):
        return self.name + ', ' + self.flavour 
