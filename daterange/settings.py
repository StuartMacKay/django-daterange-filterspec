#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os, sys

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

_ = lambda s: s
rel = lambda p: os.path.join(PROJECT_ROOT, p)

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'sqlite3',
        'NAME': 'daterrange.sqlite',
    }
}


SITE_ID = 1

TIME_ZONE = 'Europe/London'
LANGUAGE_CODE = 'en-GB'

MEDIA_ROOT = rel('../media')
MEDIA_URL = '/media/'

STATIC_ROOT = rel('static')
STATIC_URL = '/static/'

ADMIN_MEDIA_PREFIX = '/media/admin/'

ROOT_URLCONF = 'daterange.urls'

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.admin',
    'django.contrib.staticfiles',
    'daterange',
)

# Add project and fieldwork template directories so overriden
# templates are found first, rather than relying on search order
# in INSTALLED_APPS

TEMPLATE_DIRS = [
    os.path.join(PROJECT_ROOT, 'templates'),
]

SECRET_KEY = 'ju883aij5yqts@m895o0hv_208dsve)@2=x(mqiml6_(t!q@g2'
