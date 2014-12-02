from django.conf.urls import patterns, url
import re

from cal import views



urlpatterns = patterns('',
    url(r'^$', views.calendar, name='calendar'),
    url(r'^calendar/(?P<mondayParam>.*)/$', views.calendar, name='calendar'),
    
)
