from django.db import models


# Create your models here.
class TypeProducts(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(default='')
    image = models.CharField(max_length=255, default='')
    type_parent = models.IntegerField(default=0)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Products(models.Model):
    name = models.CharField(max_length=100)
    TypeProducts = models.ForeignKey(TypeProducts, on_delete=models.CASCADE)
    description = models.TextField(default='')
    unit_price = models.IntegerField(default=0)
    promotion_price = models.IntegerField(default=0)
    inventory = models.IntegerField(default=0)
    unit = models.CharField(max_length=100)
    active = models.BooleanField(default=True)
    new = models.BooleanField(default=0)
    image = models.CharField(max_length=255, default='')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

