# Generated by Django 2.2.6 on 2020-02-05 06:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0013_auto_20200205_1318'),
    ]

    operations = [
        migrations.RenameField(
            model_name='products',
            old_name='code',
            new_name='test',
        ),
    ]
