# Generated by Django 2.2.6 on 2020-02-05 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0007_auto_20200205_1309'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='code',
            field=models.CharField(blank=True, default='', max_length=30, null=True, verbose_name='Mã'),
        ),
    ]
