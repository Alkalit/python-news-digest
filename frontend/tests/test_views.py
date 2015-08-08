from django.test import TestCase
from django.db.utils import IntegrityError
from django.contrib.auth import get_user_model
from django.utils import timezone
from django.conf import settings
from django.core.urlresolvers import reverse, reverse_lazy
User = get_user_model()

from frontend.models import EditorMaterial, Tip
from frontend.views import (Sitemap, Index, IssuesList, IssueView, NewsList,
                            AddNews, ViewEditorMaterial, ItemView)


class SitemapTest():

    def setUp(self):

        self.url = reverse('frontend:sitemap')

    def test_template_used(self):

        response = self.client.get(self.url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'sitemap.html')

    def test_content_type(self):

        response = self.client.get(self.url)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content_type, 'text/xml')

    def test_context_var_domain(self):

        response = self.client.get(self.url)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['domain'], 'http://%s' % settings.BASE_DOMAIN)

    def test_context_var_record_if_no_active_issues_exists(self):

        items = [
            {
                'loc': '',
                'changefreq': 'weekly',
            },
            {
                'loc': reverse('frontend:issues'),
                'changefreq': 'weekly',
            },
            {
                'loc': reverse('frontend:feed'),
                'changefreq': 'daily',
            },
        ]

        response = self.client.get(self.url)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['records'], items)

    def test_context_var_record_if_active_issues_exists(self):

        items = [
            {
                'loc': '',
                'changefreq': 'weekly',
            },
            {
                'loc': reverse('frontend:issues'),
                'changefreq': 'weekly',
            },
            {
                'loc': reverse('frontend:feed'),
                'changefreq': 'daily',
            },
        ]

        response = self.client.get(self.url)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['records'], items)


class IndexTest(TestCase):
    pass


class IssuesListTest(TestCase):
    pass


class IssueViewTest(TestCase):
    pass


class NewsListTest(TestCase):
    pass


class AddNewsTest(TestCase):
    pass


class ViewEditorMaterialTest(TestCase):
    pass


class ItemViewTest(TestCase):
    pass
