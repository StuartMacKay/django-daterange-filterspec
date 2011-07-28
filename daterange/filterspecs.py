#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib

from django.contrib.admin.filterspecs import DateFieldFilterSpec
from django.contrib.admin.widgets import AdminDateWidget
from django.forms import Form, DateField, CharField, HiddenInput
from django.template import loader, Context

class DateRangeFilterSpec(DateFieldFilterSpec):

    extra_filter = True
    template = "admin/daterange/date_range_form.html"

    def __init__(self, f, request, params, model, model_admin, field_path=None):
        super(DateRangeFilterSpec, self).__init__(f, request, params, model,
                                                   model_admin, field_path)

        self.field_start = '%s__gte' % self.field.name
        self.field_end = '%s__lte' % self.field.name

        self.date_params = dict([(k, v) for k, v in params.items()
                                 if k.startswith(self.field_generic)])

        self.query_string = '&'.join([k+'='+urllib.quote(str(v)) for (k,v) in self.params.items()
                                      if not k.startswith(self.field_generic)])


    def output(self):
        form = self.create_form(self.params)
        
        t = loader.get_template(self.template)

        c = Context({
            'title': self.title(),
            'query': self.query_string,
            'media': getattr(self.field, 'show_media', False),
            'form': form,
        })

        return t.render(c)

    def create_form(self, params):
        form = Form()
        form.fields[self.field_start] = DateField(label='from date',
                                                  widget=AdminDateWidget,
                                                  required=False,
                                                  initial=params.get(self.field_start, ''))

        form.fields[self.field_end] = DateField(label='to date',
                                                widget=AdminDateWidget,
                                                required=False,
                                                initial=params.get(self.field_end, ''))

        for k,v in params.items():
            if not k.startswith(self.field_generic):
                form.fields[k] = CharField(widget=HiddenInput,required=False, initial=v)


        return form
