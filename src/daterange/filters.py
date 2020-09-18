import urllib

from django.contrib.admin.filters import FieldListFilter

from daterange.forms import DateRangeForm


class FormFilter(FieldListFilter):

    initial = {}
    form_class = None

    def __init__(self, field, request, params, model, model_admin, field_path):
        super().__init__(field, request, params, model, model_admin, field_path)
        expected = self.expected_parameters()
        others = {k: v for k, v in request.GET.items() if k not in expected}
        self.other_query_string = urllib.parse.urlencode(others)
        self.form = self.get_form(request)
        self.form.is_valid()

    def form_lookups(self):
        raise NotImplementedError(
            "subclasses of FormFieldFilter must provide a form_lookups() method"
        )

    def expected_parameters(self):
        return [item[0] for item in self.form_lookups()]

    def get_initial(self):
        return self.initial.copy()

    def get_form_kwargs(self, request):
        return {
            "prefix": self.field.name,
            "initial": self.get_initial(),
            "data": request.GET or None,
        }

    def get_form(self, request):
        return self.form_class(**self.get_form_kwargs(request))

    def get_lookups(self):
        lookups = {k.split("-")[1]: v for k, v in self.form_lookups()}
        data = self.form.cleaned_data if self.form.is_bound else {}
        return {v: data[k] for k, v in lookups.items() if data.get(k)}

    def queryset(self, request, queryset):
        return queryset.filter(**self.get_lookups())

    def choices(self, changelist):
        return ()


class DateRangeFilter(FormFilter):

    template = "admin/daterange/filter_form.html"
    form_class = DateRangeForm

    def form_lookups(self):
        name = self.field.name
        return (
            ("%s-start" % name, "%s__gte" % name),
            ("%s-until" % name, "%s__lt" % name),
        )
