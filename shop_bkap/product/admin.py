from django.contrib import admin
from .models import *


# Register your models here.

class InlineImage(admin.TabularInline):
    model = Images


class ProductAdmin(admin.ModelAdmin):
    inlines = [InlineImage]


admin.site.register(Products, ProductAdmin)
admin.site.register(Images)
admin.site.register(TypeProducts)
