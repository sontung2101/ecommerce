# Generated by Django 2.2.6 on 2020-02-05 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0006_auto_20200205_1309'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='code',
            field=models.CharField(blank=True, default=0, max_length=30, null=True, verbose_name='Mã'),
        ),
    ]
