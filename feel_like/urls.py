from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'feel_like.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^reservation/', include('reservations.urls')),
    url(r'', include('cal.urls')),
    
    

    #authentication urls
    url(r'^login/$', 'feel_like.views.login'),
    url(r'^auth/$', 'feel_like.views.auth_view'),
    url(r'^logout/$', 'feel_like.views.logout'),
    url(r'^home/$', 'cal.views.calendar'),
    url(r'^invalid/$', 'feel_like.views.invalid'),
)
