#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models

class Article(models.Model):
    date_added = models.DateField(auto_now_add=True)
    date_modified = models.DateField(auto_now=True)
    title = models.CharField(max_length=50)      

    # The date_range_filter attribute is used to identify which filterspec to apply.
    date_added.date_range_filter = True
    # The first filter in the extra filter panel must explicitly include the stylesheet and javascript
    # for the calendar widgets to avoid having them displayed multiple times.
    date_added.show_media = True

    # If date_range_filter is not defined then the normal DateFilterSpec will be applied.
    # date_modified.date_range_filter = True
