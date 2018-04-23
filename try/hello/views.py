# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from hello.models import Topic, Info
# Create your views here.

def help(request):
    List = Info.objects.order_by('num')
    dic = {'newr':List}
    return render(request,'index.html')
def new(request):
    List = Info.objects.order_by('num')
    dic = {'newr':List}
    return render(request,'hey.html', context =dic)
