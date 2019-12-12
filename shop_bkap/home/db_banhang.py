# # This is an auto-generated Django model module.
# # You'll have to do the following manually to clean this up:
# #   * Rearrange models' order
# #   * Make sure each model has one field with primary_key=True
# #   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
# #   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# # Feel free to rename the models, but don't rename db_table values or field names.
# from django.db import models
#
#
# class BillDetail(models.Model):
#     id_bill = models.IntegerField()
#     id_product = models.IntegerField()
#     quantity = models.IntegerField()
#     unit_price = models.FloatField()
#     created_at = models.DateTimeField()
#     updated_at = models.DateTimeField()
#
#     class Meta:
#         managed = False
#         db_table = 'bill_detail'
#
#
# class Bills(models.Model):
#     id_customer = models.IntegerField(blank=True, null=True)
#     date_order = models.DateField(blank=True, null=True)
#     total = models.FloatField(blank=True, null=True)
#     payment = models.CharField(max_length=200, blank=True, null=True)
#     note = models.CharField(max_length=500, blank=True, null=True)
#     created_at = models.DateTimeField(blank=True, null=True)
#     updated_at = models.DateTimeField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'bills'
#
#
# class Customer(models.Model):
#     name = models.CharField(max_length=100)
#     gender = models.CharField(max_length=10)
#     email = models.CharField(max_length=50)
#     address = models.CharField(max_length=100)
#     phone_number = models.CharField(max_length=20)
#     note = models.CharField(max_length=200)
#     created_at = models.DateTimeField()
#     updated_at = models.DateTimeField()
#
#     class Meta:
#         managed = False
#         db_table = 'customer'
#
#
# class News(models.Model):
#     id = models.IntegerField(primary_key=True)
#     title = models.CharField(max_length=200)
#     content = models.TextField()
#     image = models.CharField(max_length=100)
#     create_at = models.DateTimeField()
#     update_at = models.DateTimeField()
#
#     class Meta:
#         managed = False
#         db_table = 'news'
#
#
# class Products(models.Model):
#     name = models.CharField(max_length=100, blank=True, null=True)
#     id_type = models.ForeignKey('TypeProducts', models.DO_NOTHING, db_column='id_type', blank=True, null=True)
#     description = models.TextField(blank=True, null=True)
#     unit_price = models.FloatField(blank=True, null=True)
#     promotion_price = models.FloatField(blank=True, null=True)
#     image = models.CharField(max_length=255, blank=True, null=True)
#     unit = models.CharField(max_length=255, blank=True, null=True)
#     new = models.IntegerField(blank=True, null=True)
#     created_at = models.DateTimeField(blank=True, null=True)
#     updated_at = models.DateTimeField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'home'
#
#
# class Slide(models.Model):
#     link = models.CharField(max_length=100)
#     image = models.CharField(max_length=100)
#
#     class Meta:
#         managed = False
#         db_table = 'slide'
#
#
# class TypeProducts(models.Model):
#     name = models.CharField(max_length=100)
#     description = models.TextField()
#     image = models.CharField(max_length=255)
#     created_at = models.DateTimeField(blank=True, null=True)
#     updated_at = models.DateTimeField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'type_products'
#
#
# class Users(models.Model):
#     full_name = models.CharField(max_length=255)
#     email = models.CharField(unique=True, max_length=255)
#     password = models.CharField(max_length=255)
#     phone = models.CharField(max_length=20, blank=True, null=True)
#     address = models.CharField(max_length=255, blank=True, null=True)
#     remember_token = models.CharField(max_length=100, blank=True, null=True)
#     created_at = models.DateTimeField(blank=True, null=True)
#     updated_at = models.DateTimeField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'users'
