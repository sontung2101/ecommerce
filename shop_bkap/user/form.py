# from django import forms
# from django.contrib.auth.models import User
# from django.contrib.auth.forms import UserCreationForm
#
#
# # Create your models here.
# class allusers1(UserCreationForm):
#     full_name = forms.CharField(label="full_name", max_length=10)
#     phone_number = forms.CharField(label="phone_number")
#
#     class Meta:
#         model = User
#         fields = (
#             'username',
#             'password',
#             'full_name',
#             'phone_number',
#         )
#
#     def save(self, commit=True):
#         user = super(allusers1, self).save(commit=False)
#         user.username1 = self.cleaned_data['username']
#         user.password1 = self.cleaned_data['password']
#         user.phone_number = self.cleaned_data['phone_number']
#         user.full_name = self.cleaned_data['full_name']
#
#         if commit:
#             user.save()
#
#         return user
