# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.User)
admin.site.register(models.Restaurant_name)
admin.site.register(models.Rate)
admin.site.register(models.Review)
admin.site.register(models.Comment)

