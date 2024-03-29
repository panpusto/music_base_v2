from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from genres.models import Genre
from labels.models import Label
from bands.models import Band
from albums.models import Album
from reviews.models import Review


class ReviewTests(TestCase):
    
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(
            username='testuser1',
            password='testpass123',
            email='testuser1@email.com',
        )

        cls.user2 = get_user_model().objects.create_user(
            username='testuser2',
            password='testpass123',
            email='testuser2@email.com',
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
        cls.band.genre.set(str(cls.genre.id))
        cls.band.save()

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

        cls.review = Review.objects.create(
            subject='Review title',
            album=cls.album,
            band=cls.band,
            rating=10.0,
            description='Great album',
            author=cls.user
        )

    def test_review_listing_view(self):
        response = self.client.get(reverse('review_list'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(f'{self.review.subject}', 'Review title')

    def test_add_review_view_for_logged_in_user(self):
        self.client.login(
            email='testuser1@email.com',
            password='testpass123')
        response = self.client.get(reverse('add_review'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Add new review')
        self.assertNotContains(response, 'Not contain me')
        self.assertTemplateUsed(response, 'reviews/create_form.html')

    def test_add_review_for_logged_out_user(self):
        self.client.logout()
        response = self.client.get(reverse('add_review'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(
            response, f'{reverse("account_login")}?next=/reviews/add/'
        )
        response = self.client.get(
            f'{reverse("account_login")}?next=/reviews/add/'
        )
        self.assertContains(response, 'Log In')

    def test_review_detail_view(self):
        response = self.client.get(self.review.get_absolute_url())
        no_response = self.client.get('reviews/123456/')
        self.assertEqual(response.status_code, 200)  
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'Great album')
        self.assertTemplateUsed(response, 'reviews/review_detail.html')

    def test_update_view_for_author(self):
        self.client.login(
            email='testuser1@email.com',
            password='testpass123'
        )
        response = self.client.post(
            reverse(
                'review_update',
                kwargs={'pk': self.review.id}),
                {
                    'subject': 'Masterpiece',
                    'album': self.album.id,
                    'band': self.band.id,
                    'rating': 10.0,
                    'description': 'Great album',
                    'author': self.user.id
                }
        )
        self.assertEqual(response.status_code, 302)
        self.review.refresh_from_db()
        response = self.client.get(self.review.get_absolute_url())
        self.assertContains(response, 'Masterpiece')

    def test_update_view_for_non_author(self):
        self.client.login(
            email='testuser2@email.com',
            password='testpass123'
        )
        response = self.client.get(
            reverse(
                'review_update',
                kwargs={'pk': self.review.id}
            )
        )
        self.assertEqual(response.status_code, 403)
        
    def test_delete_view_for_author(self):
        self.client.login(
            email='testuser1@email.com',
            password='testpass123'
        )
        response = self.client.get(
            reverse(
                'review_delete',
                 kwargs={
                    'pk': self.review.id
                    }
                )
            )
        self.assertContains(response, 'Are you sure you want to delete review?')
        self.assertTemplateUsed(response, 'reviews/confirm_delete.html')
        post_response = self.client.post(
            reverse(
                'review_delete',
                kwargs={
                    'pk': self.review.id
                    }
                )
            )
        self.assertRedirects(
            post_response,
             reverse('review_list'),
              status_code=302)
        
    def test_delete_view_for_non_author(self):
        self.client.login(
            email='testuser2@email.com',
            password='testpass123'
        )
        response = self.client.get(
            reverse(
                'review_delete',
                kwargs={'pk': self.review.id}
            )
        )
        self.assertEqual(response.status_code, 403)