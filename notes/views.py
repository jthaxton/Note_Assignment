# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import pdb
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response
from .models import Note
import datetime
from bs4 import BeautifulSoup



def index(request):
    context = RequestContext(request, {})
    queryset = Note.objects.all()
    arr = []
    for element in queryset:
        arr.insert(0, element)
    return render(request, 'index.html', {'arr': arr})

def add_note(request):
    context = RequestContext(request, {})
    queryset = Note.objects.all()
    arr = []
    for element in queryset:
        arr.insert(0, element)

    if request.method == 'POST':
        note = BeautifulSoup(request.POST['note']).get_text()
        date = datetime.datetime.now()
        obj = Note(note_text=note, pub_date=date)
        obj.save()
        arr.insert(0,obj)
        return render(request, 'index.html', {'arr': arr})
    return render(request, 'index.html', {'arr': arr})



def delete_note(request, pk):
    context = RequestContext(request, {})
    Note.objects.get(id=pk).delete()
    queryset = Note.objects.all()
    arr = []
    for element in queryset:
        arr.insert(0, element)
    if request.method == 'POST':
            arr = []
            for element in queryset:
                arr.insert(0, element)
            return render(request, 'index.html', {'arr': arr})

