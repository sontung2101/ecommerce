# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

from django.db import models


class Slide(models.Model):
    title = models.CharField(max_length=255)
    main = models.CharField(max_length=100, null=True)
    link = models.CharField(max_length=100)
    image = models.CharField(max_length=100)

# Create your models here.
# class Question(models.Model):
#     question_text = models.CharField(max_length=200)
#     time_public = models.DateTimeField()
#
#
# class Choice(models.Model):
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)
#     choice_text = models.CharField(max_length=100)
#     vote = models.IntegerField(default=0)
