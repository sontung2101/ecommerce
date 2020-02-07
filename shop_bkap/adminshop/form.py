from django import forms
from product.models import *


class ProductForm(forms.ModelForm):
    # description = forms.CharField(max_length=500, label='Mô tả', required=False, widget=forms.Textarea)
    # image = forms.ImageField(label='Ảnh Chính')
    class Meta:
        model = Products
        fields = '__all__'


class ImageForm(forms.ModelForm):
    image = forms.ImageField(label='Ảnh phụ')

    class Meta:
        model = Images
        fields = ('image',)