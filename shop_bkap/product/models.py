from django.db import models


# Create your models here.
class TypeProducts(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(default='')
    image = models.CharField(max_length=255, default='')
    type_parent = models.IntegerField(default=0)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Products(models.Model):
    code = models.CharField(max_length=30, unique=True , default= '',verbose_name='Mã SP')  # Note unique=True,
    name = models.CharField(max_length=100,verbose_name='Tên sản phẩm')
    TypeProducts = models.ForeignKey(TypeProducts, on_delete=models.CASCADE,verbose_name='Loại sản phẩm')
    description = models.TextField(default='',verbose_name='Mô tả')
    unit_price = models.IntegerField(default=0,verbose_name='Giá SP')
    promotion_price = models.IntegerField(default=0,verbose_name='Giá KM')
    # inventory = models.IntegerField(default=0) #note
    # unit = models.CharField(max_length=100) #note
    # active = models.BooleanField(default=True) #note
    new = models.BooleanField(default=0,verbose_name='Hàng mới')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(verbose_name='Ảnh sản phẩm Chính', upload_to='images/')

    def __str__(self):
        return self.name


class Images(models.Model):
    product = models.ForeignKey(Products, default=None, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/', verbose_name='Ảnh phụ', blank=True, null=True)
