from django.db import models


class Article(models.Model):

    created = models.DateTimeField(auto_now_add=True)
    published = models.DateTimeField(null=True, blank=True)

    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    content = models.TextField()
