from django.db import models


# Create your models here.

class Partner(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    note = models.CharField(max_length=255, null=True, blank=True)
    active = models.BooleanField(default=False)
    cancel = models.BooleanField(default=False)
    customeruser_id = models.IntegerField(default=False,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
