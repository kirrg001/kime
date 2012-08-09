from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'kime.views.home', name='home'),
)
