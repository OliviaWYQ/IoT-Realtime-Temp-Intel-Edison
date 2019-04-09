#  Name:    Maoxin Hou,  Xiren Zhou, Yiqian Wang
#  UNI:   mh3895,  xz2754,  yw3225
#  Group Code: MOHA# -*- coding: utf-8 -*-


from __future__ import unicode_literals

from django.db import models
from django.utils import timezone


# Create your models here.
class TempData(models.Model):
    TempData_text = models.CharField(max_length=200)
    def __str__(self):
        return self.TempData_text