from django.test import TestCase
from django.contrib.auth import get_user_model
from musicians.models import Musician
from django.urls import reverse


class MusicianTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(
            username='testuser1',
            password='testpass123',
            email='testuser1@email.com',
        )

        cls.musician = Musician.objects.create(
            name='Musician',
            full_name='John John',
            born='1978-03-18',
            died='1978-03-18',
            place_of_birth='NY, USA',
            bio='info about musician',
            added_by=cls.user
        )

    def test_musician_listing(self):
        response = self.client.get(reverse('musician_list'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(f'{self.musician.name}', 'Musician')

    def test_add_musician_view_for_logged_in_user(self):
        self.client.login(email='testuser1@email.com', password='testpass123')
        response = self.client.get(reverse('add_musician'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Add new musician')
        self.assertNotContains(response, 'Not contain me')
        self.assertTemplateUsed(response, 'musicians/create_form.html')

    def test_add_musician_view_for_logged_out_user(self):
        self.client.logout()
        response = self.client.get(reverse('add_musician'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(
            response, f'{reverse("account_login")}?next=/musicians/add/'
        )
        response = self.client.get(
            f'{reverse("account_login")}?next=/musicians/add/'
        )
        self.assertContains(response, 'Log In')

    def test_musician_detail_view(self):
        response = self.client.get(self.musician.get_absolute_url())
        no_response = self.client.get('musicians/123456/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'info about musician')
        self.assertTemplateUsed(response, 'musicians/musician_detail.html')


# TODO:
# - change redirects urls on f-string in tests for other apps
# - add test for status_code in list views in other apps
