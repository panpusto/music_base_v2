from django.test import SimpleTestCase, TestCase
from django.urls import reverse, resolve
from django.contrib.auth import get_user_model
from labels.models import Label
from genres.models import Genre
from bands.models import Band
from musicians.models import Musician
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


class SearchTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(
            username='testuser1',
            password='testpass123',
            email='testuser1@email.com',
        )

        cls.label = Label.objects.create(
            name='2020',
            address='Warsaw',
            country='Poland',
            status=1,
            founding_year=2020,
            added_by=cls.user
        )

        cls.genre = Genre.objects.create(
            name='genre'
        )

        cls.band = Band.objects.create(
            name='Metallica',
            country_of_origin='USA',
            location='Breslau',
            status=1,
            formed_in=2000,
            ended_in=2000,
            lyrical_themes='themes',
            current_label=cls.label,
            bio='bio',
            added_by=cls.user
        )
        cls.band.genre.set(str(cls.genre.id))
        cls.band.save()

        cls.musician = Musician.objects.create(
            name='Hetfield',
            full_name='John John',
            born='1978-03-18',
            died='1978-03-18',
            place_of_birth='NY, USA',
            bio='info about musician',
            added_by=cls.user
        )

    def test_query_filter_label(self):
        searching_query = '2020'
        url = f"{reverse('search_results')}?searching_query={searching_query}"
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '2020')
        self.assertNotContains(response, 'Not contains me')
        self.assertTemplateUsed(response, 'search_results.html')

    def test_query_filter_band(self):
        searching_query = 'Metallica'
        url = f"{reverse('search_results')}?searching_query={searching_query}"
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Metallica')
        self.assertNotContains(response, 'Not contains me')
        self.assertTemplateUsed(response, 'search_results.html')

    def test_query_filter_musician(self):
        searching_query = 'Hetfield'
        url = f"{reverse('search_results')}?searching_query={searching_query}"
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Hetfield')
        self.assertNotContains(response, 'Not contains me')
        self.assertTemplateUsed(response, 'search_results.html')
        