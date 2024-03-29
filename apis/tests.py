from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from django.contrib.auth import get_user_model
from genres.models import Genre
from labels.models import Label
from bands.models import Band
from albums.models import Album
from musicians.models import Musician

class APITests(APITestCase):
    @classmethod
    def setUpTestData(cls):

        cls.user = get_user_model().objects.create_user(
            username='testuser1',
            password='testpass123',
            email='testuser1@email.com',
        )

        cls.genre = Genre.objects.create(
            name='genre'
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

        cls.musician = Musician.objects.create(
            name='Musician',
            full_name='John John',
            born='1978-03-18',
            died='1978-03-18',
            place_of_birth='NY, USA',
            bio='info about musician',
            added_by=cls.user
        )

        cls.album = Album.objects.create(
            title='Title',
            band=cls.band,
            album_type=1,
            release_date='2020-02-02',
            catalog_id='NO001',
            label=cls.label,
            album_format=1,
            cover='media/album_covers/age_of_excuse.jpg',
            added_by=cls.user
        )
        cls.album.genre.set(str(cls.genre.id))
        cls.album.save()

    def test_api_album_list_view_for_logged_in_user(self):
        self.client.login(
            email='testuser1@email.com',
            password='testpass123')
        response = self.client.get(
            reverse('api_albums_list')
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Album.objects.count(), 1)
        self.assertContains(response, self.album.title)

    def test_api_album_detail_view_for_logged_in_user(self):
        self.client.login(
            email='testuser1@email.com',
            password='testpass123')
        response = self.client.get(
            reverse(
                'api_album_detail',
                kwargs={'pk': self.album.id}),
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Album.objects.count(), 1)
        self.assertContains(response, 'NO001')

    def test_api_band_list_view_for_logged_in_user(self):
        self.client.login(
            email='testuser1@email.com',
            password='testpass123')
        response = self.client.get(
            reverse('api_bands_list')
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Band.objects.count(), 1)
        self.assertContains(response, self.band.name)

    def test_api_band_detail_view_for_logged_in_user(self):
        self.client.login(
            email='testuser1@email.com',
            password='testpass123')
        response = self.client.get(
            reverse(
                'api_band_detail',
                kwargs={'pk': self.band.id}),
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Band.objects.count(), 1)
        self.assertContains(response, 'Breslau')

    def test_api_label_list_view_for_logged_in_user(self):
        self.client.login(
            email='testuser1@email.com',
            password='testpass123')
        response = self.client.get(
            reverse('api_labels_list')
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Label.objects.count(), 1)
        self.assertContains(response, self.label)

    def test_api_label_detail_view_for_logged_in_user(self):
        self.client.login(
            email='testuser1@email.com',
            password='testpass123')
        response = self.client.get(
            reverse(
                'api_label_detail',
                kwargs={'pk': self.band.id}),
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Label.objects.count(), 1)
        self.assertContains(response, 'Warsaw')

    def test_api_musician_list_view_for_logged_in_user(self):
        self.client.login(
            email='testuser1@email.com',
            password='testpass123')
        response = self.client.get(
            reverse('api_musicians_list')
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Musician.objects.count(), 1)
        self.assertContains(response, self.musician.full_name)

    def test_api_musician_detail_view_for_logged_in_user(self):
        self.client.login(
            email='testuser1@email.com',
            password='testpass123')
        response = self.client.get(
            reverse(
                'api_musician_detail',
                kwargs={'pk': self.musician.id}),
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Musician.objects.count(), 1)
        self.assertContains(response, 'info about musician')
