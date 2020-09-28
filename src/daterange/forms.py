from django import forms
from django.contrib.admin.widgets import AdminDateWidget
from django.utils.translation import gettext_lazy as _


class DateRangeForm(forms.Form):

    start = forms.DateField(
        required=False,
        label=_("From date"),
        widget=AdminDateWidget,
    )
    until = forms.DateField(
        required=False,
        label=_("To date"),
        widget=AdminDateWidget,
    )

    def clean(self):
        start = self.cleaned_data.get("start")
        until = self.cleaned_data.get("until")

        if start and until and start >= until:
            self.add_error("start", _("From date must be earlier than To date"))
