from django.contrib import admin

from daterange.filters import DateRangeFilter

from .models import Article


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):

    list_display = ["title", "slug", "published"]
    list_filter = [("published", DateRangeFilter)]
    ordering = ["-created"]
    change_list_template = "admin/daterange/change_list.html"

    # You can avoid using the datarange changelist template
    # by including the css and javascript files directly.
    #
    # class Media:
    #     css = ("admin/css/forms.css", "css/admin/daterange.css")
    #     js = ("admin/js/calendar.js", "js/admin/DateRangeShortcuts.js")
