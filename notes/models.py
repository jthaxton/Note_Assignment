# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Note(models.Model):
    note_text = models.CharField(max_length=150)
    pub_date = models.DateTimeField('date published')
    def __unicode__(self):
        return self.note_text

# class User(models.Model):
#     username = models.CharField(max_length=15)
#     creation_date = models.DateTimeField('date published')
#     note = models.ForeignKey(Note)
#     def __str__(self):
#         return self.username