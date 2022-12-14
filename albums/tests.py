from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from labels.models import Label
from bands.models import Band
from albums.models import Album
from genres.models import Genre


class AlbumTests(TestCase):

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

    def test_albums_listing_alphabetically(self):
        response = self.client.get(
            reverse('album_list_alphabetically'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(f'{self.album.title}', 'Title')
    
    def test_add_album_view_for_logged_in_user(self):
        self.client.login(
            email='testuser1@email.com', 
            password='testpass123')
        response = self.client.get(reverse('add_album'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Add new album')
        self.assertNotContains(response, 'Not contain me')
        self.assertTemplateUsed(response, 'albums/create_form.html')

    def test_add_album_view_for_logged_out_user(self):
        self.client.logout()
        response = self.client.get(reverse('add_album'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(
            response, 
            f'{reverse("account_login")}?next=/albums/add/'
        )
        response = self.client.get(
            f'{reverse("account_login")}?next=/albums/add/'
        )
        self.assertContains(response, 'Log In')
    
    def test_album_detail_view(self):
        response = self.client.get(self.album.get_absolute_url())
        no_response = self.client.get('albums/123456/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'NO001')
        self.assertTemplateUsed(response, 'albums/album_detail.html')

    def test_album_update_view_for_logged_in_user(self):
        self.client.login(
            email='testuser1@email.com',
            password='testpass123')
        response = self.client.post(
            reverse('album_update',
            kwargs={'pk': self.album.id}),
            {
                'title': 'Axiom',
                'band': self.band.id,
                'album_type': 1,
                'catalog_id': 'NO001',
                'label': self.label.id,
                'release_date': '2020-02-02',
                'genre': self.genre.id,
                'album_format': 1,
                'cover': 'media/album_covers/age_of_excuse.jpg',
                'added_by': self.user.id
            })
        # print(response.context['form'].errors) - checking errors in form
        self.assertEqual(response.status_code, 302)
        self.album.refresh_from_db()
        response = self.client.get(self.album.get_absolute_url())
        self.assertContains(response, 'Axiom')

    def test_album_update_view_for_logged_out_user(self):
        self.client.logout()
        response = self.client.get(
            reverse('album_update', kwargs={'pk': self.album.id}))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(
            response,
            f'{reverse("account_login")}?next=/albums/update/{self.album.id}/'
        )
        response = self.client.get(
            f'{reverse("account_login")}?next=/albums/update/{self.album.id}/'
        )
        self.assertContains(response, 'Log In')
