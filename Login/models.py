# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

# Create your models here.


class User(models.Model):
    user_id = models.AutoField(unique=True, primary_key=True)
    username = models.CharField(max_length=10, unique=True)
    password = models.CharField(max_length=12)

    def __str__(self):
        return self.username


class Restaurant_name(models.Model):
    Rest_id = models.AutoField(unique=True, primary_key=True)
    Rest_name = models.CharField(max_length=50, unique=True)
    address = models.CharField(max_length=200)
    ave_rate = models.FloatField(default='0')
    review = models.ManyToManyField(User, through='Review', related_name='review_user')
    rate = models.ManyToManyField(User, through='Rate')
    img = models.ImageField(upload_to='img',default='')
    category = models.CharField(max_length=20 ,default='')

    def __str__(self):
       return self.Rest_name


class Rate(models.Model):
    userid = models.ForeignKey(User, on_delete=models.CASCADE,related_name='userId_user')
    restid = models.ForeignKey(Restaurant_name, on_delete=models.CASCADE, related_name='restId_rest')
    rate = models.IntegerField()

class Review(models.Model):
    reviewId = models.AutoField(unique=True, primary_key=True)
    ownerUserId = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owner_user')
    restId = models.ForeignKey(Restaurant_name, on_delete=models.CASCADE, related_name='rest_rest')
    content = models.CharField(max_length=500)


class Comment(models.Model):
    subCommentId = models.AutoField(unique=True, primary_key=True)
    review = models.ForeignKey("Review", on_delete=models.CASCADE)
    commentUserName = models.CharField(max_length=10,default='o')
    content = models.CharField(max_length=400)
