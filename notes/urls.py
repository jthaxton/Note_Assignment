from django.contrib import admin
from django.urls import include, path
from django.conf.urls import url
from . import views


urlpatterns = [ 
    # path('', index, name='index'),
    url(r'^$', views.index, name='index'),
    url(r'^notes/add_note/$', views.add_note, name='add_note'),
    url(r'^notes/(?P<pk>\w+)/delete_note$', views.delete_note, name='delete_note'),
]
