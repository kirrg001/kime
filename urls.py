from django.conf.urls import patterns, include, url
from kime.views import *

urlpatterns = patterns('',
    url(r'^$', home),
)
