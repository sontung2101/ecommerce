# Generated by Django 2.2.6 on 2019-12-19 04:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0003_partner_cancel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='partner',
            name='active',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='partner',
            name='cancel',
            field=models.BooleanField(default=False),
        ),
    ]