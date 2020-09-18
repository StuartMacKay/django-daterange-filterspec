Django DateRange Filterspec
===========================

Adds a form with AdminDateWidgets that can be used to select a range of
dates for filtering the list of records displayed in an admin Changelist.

.. image:: https://raw.githubusercontent.com/StuartMacKay/django-daterange-filterspec/master/docs/images/screenshot.png

Quick start
-----------

Install the package from PyPI::

    pip install django-daterange-filterspec

The package includes a template, which loads Django's calendar widget
and date shortcuts. Your templates can either this this template as a
parent::

    {% extends "admin/daterange/change_list.html" %}

or, copy the ``extrastyle`` and ``extrahead`` blocks from this template
to your own.

In your ModelAdmin, for each filter you want to filter on create a tuple
with the name of the field and the ``DateRangeFilter`` filter class::

    from django.contrib import admin

    from daterange.filters import DateRangeFilter

    from .models import Article


    @admin.register(Article)
    class ArticleAdmin(admin.ModelAdmin):

        list_display = ["title", "slug", "published"]
        list_filter = [("published", DateRangeFilter)]
        ordering = ["-created"]

Now, go forth and filter!

Project
-------

If you check out the project from the repository there is a fully functioning
Django site that you can use to see the filter in action.
