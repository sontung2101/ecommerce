# Generated by Django 2.2.6 on 2020-02-05 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0017_auto_20200205_1324'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='code',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
