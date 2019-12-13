from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from user.models import CustomerUser


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomerUser
        fields = "__all__"


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomerUser
        fields = "__all__"