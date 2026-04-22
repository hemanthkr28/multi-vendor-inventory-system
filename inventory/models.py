from django.db import models

class Vendor(models.Model):
    name = models.CharField(max_length=100)

class Product(models.Model):
    product_name = models.CharField(max_length=100)

class Inventory(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    price = models.FloatField()
    stock = models.IntegerField()