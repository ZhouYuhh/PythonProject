# Generated by Django 2.2 on 2019-04-23 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Login', '0005_restaurant_name_ave_rate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant_name',
            name='ave_rate',
            field=models.FloatField(default='0'),
        ),
    ]
