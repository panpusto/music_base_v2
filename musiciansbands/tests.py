from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from musicians.models import Musician
from labels.models import Label
from bands.models import Band
from musiciansbands.models import MusicianBand


class MusicianToBandTests(TestCase):

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

        cls.label = Label.objects.create(
            name='2020',
            address='Warsaw',
            country='Poland',
            status=1,
            founding_year=2020,
            added_by=cls.user
        )

        cls.band = Band.objects.create(
            name='Band',
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

        cls.musiciantoband = MusicianBand.objects.create(
            musician=cls.musician,
            band=cls.band,
            year_from=2000,
            year_to=2000,
            role='guitarist'
        )

    def test_add_musician_to_band_view_for_logged_in_user(self):
        self.client.login(email='testuser1@email.com', password='testpass123')
        response = self.client.get(reverse('add_musician_to_band'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Add musician to band')
        self.assertNotContains(response, 'Not contain me')
        self.assertTemplateUsed(response, 'musiciansbands/create_form.html')

    def test_add_musician_to_band_view_for_logged_out_user(self):
        self.client.logout()
        response = self.client.get(reverse('add_musician_to_band'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(
            response, f'{reverse("account_login")}?next=/musiciantoband/add/'
        )
        response = self.client.get(
            f'{reverse("account_login")}?next=/musiciantoband/add/'
        )
        self.assertContains(response, 'Log In')
        