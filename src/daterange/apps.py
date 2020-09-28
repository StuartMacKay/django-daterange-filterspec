from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class DateRangeFilterConfig(AppConfig):
    name = "daterange"
    verbose_name = _("DateRange Filter")
