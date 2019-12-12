from django.db import models
from product.models import Products
from order.models import Partner


# Create your models here.

class Cart(models.Model):
    Partner = models.ForeignKey(Partner, on_delete=models.CASCADE)
    total = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class CartItem(models.Model):
    Cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    Products = models.ForeignKey(Products, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    unit_price = models.FloatField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
