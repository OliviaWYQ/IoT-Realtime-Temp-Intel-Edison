#  Name:    Maoxin Hou,  Xiren Zhou, Yiqian Wang
#  UNI:   mh3895,  xz2754,  yw3225
#  Group Code: MOHA# -*- coding: utf-8 -*-


from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import TempData

admin.site.register(TempData)