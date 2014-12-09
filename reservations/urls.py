from django.conf.urls import patterns, url
import re

from reservations import views

urlpatterns = patterns('',
	url(r'^list/?$', views.list, name='r_list'),
    url(r'^create/?$', views.create, name='r_create'),
    url(r'^edit/(?P<reservationId>\d+)/$', views.edit, name='r_edit'),
    url(r'^delete/(?P<reservationId>\d+)/$', views.delete, name='r_delete'),
    url(r'^customer/(?P<id>\d+)/delete/$', views.customer_delete,
        name='customer_delete'),
    url(r'^customer/(?P<id>\d+)/$', views.customer_edit,
        name='customer_edit'),
    url(r'^customer/$', views.customer_list, name='customer_list'),

    url(r'^coach/$', views.coach_list, name='coach_list'),
    url(r'^coach/(?P<id>\d+)/$', views.coach_edit,
        name='coach_edit'),
    url(r'^coach/(?P<id>\d+)/delete/$', views.coach_delete,
        name='coach_delete'),
    url(r'^company/$', views.company_edit,
        name='company_edit'),
    url(r'^invoice/create/$', views.invoice_create, name='invoice_create'),
    url(r'^invoice/calculate_total/$', views.calculate_total,
        name='calculate_total'),
    url(r'^invoice/invoice_list/$', views.invoice_list,
        name='invoice_list'),
    url(r'^invoice/(?P<id>\d+)/delete/$', views.invoice_delete,
        name='invoice_delete'),
)
