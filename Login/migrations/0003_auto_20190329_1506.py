# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-03-29 07:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Login', '0002_delete_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rate', models.IntegerField(max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Restaurant_name',
            fields=[
                ('Rest_id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('Rest_name', models.CharField(max_length=50, unique=True)),
                ('address', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('username', models.CharField(max_length=10, unique=True)),
                ('password', models.CharField(max_length=12)),
            ],
        ),
        migrations.AddField(
            model_name='restaurant_name',
            name='rates',
            field=models.ManyToManyField(through='Login.Rate', to='Login.User'),
        ),
        migrations.AddField(
            model_name='rate',
            name='restid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Login.Restaurant_name'),
        ),
        migrations.AddField(
            model_name='rate',
            name='userid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Login.User'),
        ),
    ]