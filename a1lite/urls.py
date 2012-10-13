# -*- coding: utf-8 -*-

from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('a1lite.views',
    url(r'^process/$', 'process', name='a1lite_process'),
    url(r'^success/$', 'success', name='a1lite_success'),
    url(r'^error/$', 'error', name='a1lite_error'),
 )
