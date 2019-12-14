from django.contrib import admin
from user.models import CustomerUser
from django.contrib.auth.admin import UserAdmin

# Register your models here.
admin.site.register(CustomerUser, UserAdmin)
