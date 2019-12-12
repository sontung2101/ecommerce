from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class CustomerUser(AbstractUser):
    name = models.CharField(max_length=255,null=True,blank=True)
    phone_number = models.CharField(max_length=12, null=True,blank=True)
    address = models.CharField(max_length=255,null=True,blank=True)
