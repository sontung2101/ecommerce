from django import forms
from order.models import Partner


class oderForm(forms.ModelForm):
    class Meta:
        model = Partner
        fields = "__all__"
        widgets = {
            'name': forms.TextInput(attrs={'class': 'size13 bo4 m-b-12 sizefull s-text7 p-l-15 p-r-15', 'placeholder': 'Name','style':'border:1px solid #e6e6e6 !important ;max-width:500px;height :50px;padding: 7px ; font-size :20px '}),
            'email': forms.TextInput(attrs={'class': 'size13 bo4 m-b-12 sizefull s-text7 p-l-15 p-r-15', 'placeholder': 'Email','style': 'border:1px solid #e6e6e6 !important;max-width:500px;height :50px; padding: 7px ; font-size :20px'}),
            'address': forms.TextInput(attrs={'class': 'size13 bo4 m-b-12 sizefull s-text7 p-l-15 p-r-15', 'placeholder': 'Address','style': 'border:1px solid #e6e6e6 !important ;max-width:500px;height :50px; padding: 7px ; font-size :20px'}),
            'phone_number': forms.TextInput(attrs={'class': 'size13 bo4 m-b-12 sizefull s-text7 p-l-15 p-r-15', 'placeholder': 'Phone number','style': 'border:1px solid #e6e6e6 !important;max-width:500px;height :50px; padding: 7px ; font-size :20px'}),
            'note': forms.Textarea(attrs={'class': 'size13 bo4 m-b-12 sizefull s-text7 p-l-15 p-r-15', 'placeholder': 'Note','style': 'border:1px solid #e6e6e6 !important ;max-width:500px;height :50px; padding: 7px ; font-size :20px;height:200px;resize: none;'}),
        }
