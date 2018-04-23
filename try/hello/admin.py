# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from hello.models import Topic, Info

# Register your models here.
admin.site.register(Topic)
admin.site.register(Info)
