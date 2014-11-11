from django.conf.urls import patterns, url
import re

from reservations import views

urlpatterns = patterns('',
	url(r'^create/?$', views.create),
    url(r'^edit/(?P<reservationId>\d+)/$', views.edit),
	url(r'^delete/(?P<reservationId>\d+)/$', views.delete),
)