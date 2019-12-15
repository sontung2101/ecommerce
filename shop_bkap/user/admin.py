# users/admin.py
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .form import MyUserCreationForm, MyUserChangeForm
from .models import CustomerUser


class MyUserAdmin(UserAdmin):
    add_form = MyUserCreationForm
    form = MyUserChangeForm
    model = CustomerUser
    list_display = ['username', 'full_name', 'phone_number']
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('full_name', 'phone_number')}),
    )  # this will allow to change these fields in admin module


admin.site.register(CustomerUser, MyUserAdmin)
