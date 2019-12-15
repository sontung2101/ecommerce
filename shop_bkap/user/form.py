from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomerUser


class MyUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomerUser
        fields = ('username', 'full_name', 'phone_number')


class MyUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm):
        model = CustomerUser
        fields = ('username', 'full_name', 'phone_number')
