from django.http import HttpRequest
from django.test import TestCase
from django.urls import resolve

from snippets.views import top, snippet_new, snippet_edit, snippet_detail

class TopPageTest(TestCase):
    def test_top_page_returns_200_and_expected_title(self):
        response = self.client.get('/')
        self.assertContains(response, 'Djangoスニペット', status_code=200)

    def test_top_page_uses_expected_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'snippets/top.html')

class CreateSnippetTest(TestCase):
    def test_should_resolve_snippet_new(self):
        found = resolve('/snippets/new/')
        self.assertEqual(snippet_new, found.func)

class SnippetDetailTest(TestCase):
    def test_should_resolve_snippet_detail(self):
        found = resolve('/snippets/1/')
        self.assertEqual(snippet_detail, found.func)

class EditSnippetTest(TestCase):
    def test_should_resolve_snippet_edit(self):
        found = resolve('/snippets/1/edit/')
        self.assertEqual(snippet_edit, found.func)
