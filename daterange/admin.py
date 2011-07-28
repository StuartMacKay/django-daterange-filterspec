#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.contrib import admin
from django.contrib.admin.filterspecs import FilterSpec

from models import Article
from filterspecs import DateRangeFilterSpec

class ArticleAdmin(admin.ModelAdmin):
    list_display = ['date_added', 'date_modified', 'title']
    list_filter = ['date_added', 'date_modified']
    ordering = ['-date_added']


admin.site.register(Article, ArticleAdmin)

# register the date-range filter spec
FilterSpec.filter_specs.insert(0, (lambda f: hasattr(f, 'date_range_filter'), DateRangeFilterSpec))
