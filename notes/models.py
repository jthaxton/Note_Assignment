# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Note(models.Model):
    note_text = models.CharField(max_length=150)
    pub_date = models.DateTimeField('date published')
    def __unicode__(self):
        return self.note_text

    



