# Generated by Django 2.2 on 2019-05-04 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Login', '0009_auto_20190427_1730'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='commentUserId',
        ),
        migrations.AddField(
            model_name='comment',
            name='commentUserName',
            field=models.CharField(default='o', max_length=10),
        ),
    ]