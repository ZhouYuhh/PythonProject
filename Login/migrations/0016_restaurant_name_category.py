# Generated by Django 2.2 on 2019-05-31 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Login', '0015_auto_20190530_1715'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant_name',
            name='category',
            field=models.CharField(default='', max_length=20),
        ),
    ]
