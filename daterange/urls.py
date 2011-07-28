#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf import settings
from django.conf.urls.defaults import *
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    (r'^admin/', include(admin.site.urls)),    
)

urlpatterns += patterns('django.views.static',
    (r'^%s(?P<path>.*)$' % settings.STATIC_URL[1:] , 'serve', 
     {'document_root': settings.STATIC_ROOT}),
    (r'^%s(?P<path>.*)$' % settings.MEDIA_URL[1:] , 'serve',
     {'document_root': settings.MEDIA_ROOT}),
)
