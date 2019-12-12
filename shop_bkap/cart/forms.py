from django import forms
from cart.models import Cart


class cartForm(forms.ModelForm):
    class Meta:
        model = Cart
        fields = "__all__"
