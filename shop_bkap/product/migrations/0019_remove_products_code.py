# Generated by Django 2.2.6 on 2020-02-05 06:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0018_products_code'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='products',
            name='code',
        ),
    ]