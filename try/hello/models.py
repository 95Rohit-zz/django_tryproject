# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Topic(models.Model):
    ID_number = models.CharField(max_length=30,unique = True)

    def __str__(self):
        return self.ID_number

class Info(models.Model):
    num = models.ForeignKey(Topic,on_delete=models.CASCADE)
    First = models.CharField(max_length=30,)
    Last = models.CharField(max_length=30,)
    email = models.EmailField(max_length=30,unique = True)

    def __str__(self):
        return self.First
