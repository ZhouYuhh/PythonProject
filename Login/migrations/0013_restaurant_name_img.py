# Generated by Django 2.2 on 2019-05-24 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Login', '0012_delete_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant_name',
            name='img',
            field=models.ImageField(default='', upload_to='img'),
        ),
    ]
