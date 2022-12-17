from django.test import TestCase
from django.contrib.auth import get_user_model
from bands.models import Band
from django.urls import reverse


class BandTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(
            username='testuser1',
            password='testpass123',
            email='testuser1@email.com',
        )

        cls.band = Band.objects.create(
            name='Band',
            country_of_origin='USA',
            location='Breslau',
            status=1,
            formed_in=2000,
            ended_in=2000,
            genre=[1],
            lyrical_themes='themes',
            current_label=1,
            bio='bio',
            added_by=cls.user
        )

    def test_bands_listing_alphabetically(self):
        response = self.client.get(reverse('band_list_alphabetically'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(f'{self.band.name}', 'Band')

    # def test_add_musician_view_for_logged_in_user(self):
    #     self.client.login(email='testuser1@email.com', password='testpass123')
    #     response = self.client.get(reverse('add_musician'))
    #     self.assertEqual(response.status_code, 200)
    #     self.assertContains(response, 'Add new musician')
    #     self.assertNotContains(response, 'Not contain me')
    #     self.assertTemplateUsed(response, 'musicians/create_form.html')

    # def test_add_musician_view_for_logged_out_user(self):
    #     self.client.logout()
    #     response = self.client.get(reverse('add_musician'))
    #     self.assertEqual(response.status_code, 302)
    #     self.assertRedirects(
    #         response, f'{reverse("account_login")}?next=/musicians/add/'
    #     )
    #     response = self.client.get(
    #         f'{reverse("account_login")}?next=/musicians/add/'
    #     )
    #     self.assertContains(response, 'Log In')

    # def test_musician_detail_view(self):
    #     response = self.client.get(self.musician.get_absolute_url())
    #     no_response = self.client.get('musicians/123456/')
    #     self.assertEqual(response.status_code, 200)
    #     self.assertEqual(no_response.status_code, 404)
    #     self.assertContains(response, 'info about musician')
    #     self.assertTemplateUsed(response, 'musicians/musician_detail.html')

    # TODO:
    # - add label instance