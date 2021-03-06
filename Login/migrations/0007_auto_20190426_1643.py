# Generated by Django 2.2 on 2019-04-26 08:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Login', '0006_auto_20190423_1607'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='restaurant_name',
            name='rates',
        ),
        migrations.AddField(
            model_name='restaurant_name',
            name='rate',
            field=models.ManyToManyField(related_name='rate_user', through='Login.Rate', to='Login.User'),
        ),
        migrations.AlterField(
            model_name='rate',
            name='restid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='restId_rest', to='Login.Restaurant_name'),
        ),
        migrations.AlterField(
            model_name='rate',
            name='userid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='userId_user', to='Login.User'),
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('reviewId', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('content', models.CharField(max_length=500)),
                ('likeCount', models.IntegerField()),
                ('likeUser', models.IntegerField()),
                ('ownerUserId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='owner_user', to='Login.User')),
                ('restId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rest_rest', to='Login.Restaurant_name')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('subCommentId', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('commentUserId', models.IntegerField()),
                ('content', models.CharField(max_length=400)),
                ('review', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Login.Review')),
            ],
        ),
        migrations.AddField(
            model_name='restaurant_name',
            name='review',
            field=models.ManyToManyField(related_name='review_user', through='Login.Review', to='Login.User'),
        ),
    ]
