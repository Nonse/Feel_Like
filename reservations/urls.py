from django.conf.urls import patterns, url
import re

from reservations import views

urlpatterns = patterns('',
	url(r'^create/?$', views.create),
    url(r'^edit/(?P<reservationId>\d+)/$', views.edit),
	url(r'^delete/(?P<reservationId>\d+)/$', views.delete),
	url(r'^customer/(?P<id>\d+)/delete/$', views.customer_delete,
		name='customer_delete'),
	url(r'^customer/(?P<id>\d+)/$', views.customer_edit,
		name='customer_edit'),
	url(r'^customer/$', views.customer_list, name='customer_list'),
)
