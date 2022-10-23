from django.test import SimpleTestCase
from django.urls import reverse, resolve

from .views import HomePageView


class HomePageTests(SimpleTestCase):
    def setUp(self):
        url = reverse('home')
        self.response = self.client.get('/')

    def test_urls_exists_at_correct_location(self):
        self.assertEqual(self.response.status_code, 200)

    def test_homepage_url_name(self):
        self.assertEqual(self.response.status_code, 200)

    def test_homepage_template(self):
        self.assertTemplateUsed(self.response, 'home.html')

    def test_homepage_contains_correct_html(self):
        self.assertContains(self.response, 'home page')

    def test_homepage_not_contains_incorrect_html(self):
        self.assertNotContains(self.response, 'Not contain me!')

    def test_homepage_url_resolves_homepageview(self):
        view = resolve('/')
        self.assertEqual(view.func.__name__, HomePageView.as_view().__name__)
