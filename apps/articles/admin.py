from django.contrib import admin

from daterange.filters import DateRangeFilter

from .models import Article


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):

    list_display = ["title", "slug", "published"]
    list_filter = [("published", DateRangeFilter)]
    ordering = ["-created"]
