# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render
from .models import Update

def index(request):
    #return HttpResponse('Hello from cl')
    update= Update.objects.all()[:10]
    context ={
        'title': 'Latest Update',
        'update':update
    }

    return render(request,'cl/index.html',context)

def details(request, id):
    update=Update.objects.get(id=id)
    context={
        'update':update
    }
    return render(request, 'cl/details.html', context)