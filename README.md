# Django DateRange Filterspec

Adds a form with AdminDateWidgets that can be used to select a range of
dates for filtering the list of records displayed in an admin Changelist.

![Filter list](https://raw.githubusercontent.com/StuartMacKay/django-daterange-filterspec/master/docs/images/screenshot.png)

The `From date` selects records with a date equal or greater than the 
specified date. The `To date` selects record up to, but not including
the specified date. Either field is optional. If you only enter a date 
in the `From date` field then all records from that date onwards will be
displayed. Similarly if you only enter a date in the `To date` field then
only records before that date will be displayed.

## Quick start

Install the package from PyPI:

```shell
pip install django-daterange-filterspec
```

The package includes a template, which loads Django's calendar widget
and date shortcuts. Add the package to the INSTALLED_APPS setting so the
template loader can find it:

```python
INSTALLED_APPS = (
    ...
    "daterange.apps.DateRangeFilterConfig",
    ...
)
```

In your ModelAdmin, set the template used for the changelist to the one
provided by the package. Then, for each field you want to filter on
create a tuple with the name of the field and the `DateRangeFilter`
filter class:

```python
from django.contrib import admin

from daterange.filters import DateRangeFilter

from .models import Article


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):

    list_display = ["title", "slug", "published"]
    list_filter = [("published", DateRangeFilter)]
    ordering = ["-created"]

    change_list_template = "admin/daterange/change_list.html"
```

If you're already using a customised changelist template, you can add the necessary
css and javascript files to the Media class for the ModelAdmin:

```python
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):

    ...

    class Media:
        css = {"all": ("admin/css/forms.css", "css/admin/daterange.css")}
        js = ("admin/js/calendar.js", "js/admin/DateRangeShortcuts.js")
```

Now, go forth and filter!

## Demo

If you check out the project from the repository there is a fully functioning
Django site that you can use to see the filter in action.

```shell
git clone git@github.com:StuartMacKay/django-daterange-filterspec.git
cd django-daterange-filterspec
```

Create the virtual environment:

```shell
python -m venv venv
source venv/bin/activate

pip install --upgrade pip setuptools wheel
pip install pip-tools
pip-sync requirements/dev.txt
```

Run the demo:

```shell
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Now log into the Django Admin. In the Demo section, add some Articles
for different dates and filter away.
