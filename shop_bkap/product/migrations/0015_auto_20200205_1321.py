# Generated by Django 2.2.6 on 2020-02-05 06:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0014_auto_20200205_1319'),
    ]

    operations = [
        migrations.RenameField(
            model_name='products',
            old_name='unit',
            new_name='code',
        ),
        migrations.RemoveField(
            model_name='products',
            name='test',
        ),
    ]
