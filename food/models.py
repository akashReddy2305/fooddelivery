from django.db import models

class Organization(models.Model):
    name = models.CharField(max_length=100)

class Item(models.Model):
    type = models.CharField(max_length=100)
    description = models.TextField()

class Pricing(models.Model):
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    zone = models.CharField(max_length=100)
    base_distance_in_km = models.DecimalField(max_digits=10, decimal_places=2)
    km_price = models.DecimalField(max_digits=10, decimal_places=2)
    fix_price = models.DecimalField(max_digits=10, decimal_places=2)
