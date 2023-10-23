from datetime import timedelta

from django.contrib.admin import site
from django.contrib.auth.models import User
from django.test import RequestFactory, TestCase
from django.utils import timezone

import pytest

from demo.admin import ArticleAdmin
from demo.models import Article


@pytest.mark.django_db
class DateRangeFilterTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.model = Article
        cls.user = User.objects.create_user(username="user", password="password")
        cls.objects = [
            Article.objects.create(
                title="First article",
                slug="first-article",
                content="Contents of the first article",
                published=timezone.now() - timedelta(days=1),
            ),
            Article.objects.create(
                title="Second article",
                slug="second-article",
                content="Contents of the second article",
                published=timezone.now(),
            ),
            Article.objects.create(
                title="Third article",
                slug="third-article",
                content="Contents of the third article",
                published=timezone.now() + timedelta(days=1),
            ),
            Article.objects.create(
                title="Fourth article",
                slug="fourth-article",
                content="Contents of the fourth article",
                published=None,
            ),
        ]

    def setUp(self) -> None:
        super().setUp()
        self.model_admin = ArticleAdmin(Article, site)

    def get_request(self, path="/", data=None):
        request_factory = RequestFactory()
        request = request_factory.get(path, data=data)
        request.user = self.user
        return request

    def get_changelist(self, request):
        return self.model_admin.get_changelist_instance(request)

    def get_queryset(self, request):
        return self.get_changelist(request).get_queryset(request)

    def get_filter(self, request):
        return self.get_changelist(request).get_filters(request)[0][0]

    def get_date(self, obj):
        return obj.published.strftime("%Y-%m-%d")

    def test_template(self):
        """Verify the correct template is used to render the form."""
        request = self.get_request("/")
        filterspec = self.get_filter(request)
        self.assertEqual(filterspec.template, "admin/daterange/filter_form.html")

    def test_title(self):
        """The filter title is the name of the field."""
        request = self.get_request("/")
        filterspec = self.get_filter(request)
        self.assertEqual(filterspec.title, "published")

    def test_from_start_date(self):
        """The queryset only includes objects from the start date or later."""
        date = self.get_date(self.objects[1])
        request = self.get_request("/", {"published-start": date})
        expected = Article.objects.filter(published__gte=date).order_by("-created")
        actual = self.get_queryset(request)
        self.assertListEqual(list(expected), list(actual))

    def test_until_end_date(self):
        """The queryset only includes objects earlier than the end date."""
        date = self.get_date(self.objects[1])
        request = self.get_request("/", {"published-until": date})
        expected = Article.objects.filter(published__lt=date)
        actual = self.get_queryset(request)
        self.assertListEqual(list(expected), list(actual))

    def test_null_dates_are_excluded(self):
        """Objects with null dates are not considered earlier than the end date."""
        date = self.get_date(self.objects[1])
        request = self.get_request("/", {"published-until": date})
        queryset = self.get_queryset(request).filter(published__isnull=True)
        self.assertEqual(queryset.count(), 0)

    def test_invalid_start_date(self):
        """An invalid start date is reported as a validation error on the form."""
        request = self.get_request("/", {"published-start": "2020-13-32"})
        filterspec = self.get_filter(request)
        self.assertIn("start", filterspec.form.errors)

    def test_invalid_end_date(self):
        """An invalid end date is reported as a validation error on the form."""
        request = self.get_request("/", {"published-until": "2020-13-32"})
        filterspec = self.get_filter(request)
        self.assertIn("until", filterspec.form.errors)

    def test_form_invalid(self):
        """The queryset is not filtered if there is an error on the form."""
        request = self.get_request("/", {"published-start": "2020-13-32"})
        expected = Article.objects.all().order_by("-created")
        actual = self.get_queryset(request)
        self.assertListEqual(list(expected), list(actual))
