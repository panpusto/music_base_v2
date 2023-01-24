from django.test import TestCase
from django.contrib.auth import get_user_model
from genres.models import Genre
from django.urls import reverse

class GenreTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(
            username = 'testuser',
            password = 'testpass123',
            email = 'testuser@email.com',
        )

        cls.genre = Genre.objects.create(
            name = 'test genre'
        )

    def test_genre_listing(self):
        response = self.client.get(reverse('genre_list'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(f'{self.genre.name}', 'test genre')

    def test_add_genre_view_for_logged_in_user(self):
        self.client.login(
            email='testuser@email.com',
            password='testpass123')
        response = self.client.get(reverse('add_genre'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Add new genre')
        self.assertNotContains(response, 'Not contain me')
        self.assertTemplateUsed(response, 'genres/create_form.html')

    def test_add_genre_view_for_logged_out_user(self):
        self.client.logout()
        response = self.client.get(reverse('add_genre'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(
            response, f'{reverse("account_login")}?next=/genres/add/'
        )
        response = self.client.get(
            f'{reverse("account_login")}?next=/genres/add/'
        )
        self.assertContains(response, 'Log In')
        