from django.conf.urls import patterns, include, url
from kime.views import *
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', home),
    url(r'^login$', user_login),
    url(r'^logout$', user_logout),
    url(r'^admin/', include(admin.site.urls)),
)
