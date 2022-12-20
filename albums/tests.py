from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from labels.models import Label
from bands.models import Band
from albums.models import Album


class AlbumTests(TestCase):

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

        cls.album = Album.objects.create(
            title='Title',
            band=cls.band,
            album_type=1,
            release_date='2020-02-02',
            catalog_id='NO001',
            label=cls.label,
            album_format=1,
            added_by=cls.user
        )

    def test_albums_listing_alphabetically(self):
        response = self.client.get(reverse('album_list_alphabetically'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(f'{self.album.title}', 'Title')
    
    