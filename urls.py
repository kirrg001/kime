from django.conf.urls import patterns, include, url
from kime.views import *
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', home),
    url(r'^login$', user_login),
    url(r'^projects/', projects),
    url(r'^save_time_entry/$', save_time_entry),
    url(r'^remove_time_entry/$', remove_time_entry),
    url(r'^update_time_entry/$', update_time_entry),
    url(r'^logout$', user_logout),
    url(r'^admin/', include(admin.site.urls)),
)
