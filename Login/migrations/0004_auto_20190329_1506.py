# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-03-29 07:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Login', '0003_auto_20190329_1506'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rate',
            name='rate',
            field=models.IntegerField(),
        ),
    ]
