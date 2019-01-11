# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import pdb
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Note
import datetime
from bs4 import BeautifulSoup
from forms import NoteForm


def index(request):
    queryset = Note.objects.all()
    arr = []
    for element in queryset:
        arr.insert(0, element)
    return render(request, 'index.html', {'arr': arr})

def add_note(request):
    if NoteForm(request.POST).is_valid():
        note = BeautifulSoup(request.POST['note']).get_text()
        date = datetime.datetime.now()
        obj = Note(note_text=note, pub_date=date)
        obj.save()
        return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/')

def delete_note(request, id):
    Note.objects.get(id=id).delete()
    return HttpResponseRedirect('/')

