# Generated by Django 2.2.6 on 2019-12-01 07:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='date_order',
        ),
    ]
