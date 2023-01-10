from django.test import TestCase
from django.contrib.auth import get_user_model
from labels.models import Label
from django.urls import reverse


class LabelTests(TestCase):

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
            added_by=cls.user,
            styles='rock'
        )

    def test_label_listing(self):
        response = self.client.get(reverse('label_list'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(f'{self.label.name}', '2020') 

    def test_add_label_view_for_logged_in_user(self):
        self.client.login(
            email='testuser1@email.com',
            password='testpass123')
        response = self.client.get(reverse('add_label'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Add new label')
        self.assertNotContains(response, 'Not contain me')
        self.assertTemplateUsed(response, 'labels/create_form.html')

    def test_add_label_view_for_logged_out_user(self):
        self.client.logout()
        response = self.client.get(reverse('add_label'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(
            response,
            f'{reverse("account_login")}?next=/labels/add/'
        )
        response = self.client.get(
            f'{reverse("account_login")}?next=/labels/add/'
        )   
        self.assertContains(response, 'Log In')

    def test_label_detail_view(self):
        response = self.client.get(self.label.get_absolute_url())
        no_response = self.client.get('labels/123456/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'Warsaw')
        self.assertTemplateUsed(response, 'labels/label_detail.html')

    def test_label_update_view_for_logged_in_user(self):
        self.client.login(
            email='testuser1@email.com',
            password='testpass123'
        )
        response = self.client.post(
            reverse(
                'label_update',
                kwargs={'pk': self.label.id}),
                {
                    'name': 'Terratur',
                    'address': 'Warsaw',
                    'country': 'Poland',
                    'status': 1,
                    'founding_year': 2020,
                    'added_by': self.user.id,
                    'styles': 'rock'
                }
        )
        self.assertEqual(response.status_code, 302)
        self.label.refresh_from_db()
        response = self.client.get(self.label.get_absolute_url())
        self.assertContains(response, 'Terratur')

    def test_label_update_view_for_logged_out_user(self):
        self.client.logout()
        response = self.client.get(
            reverse(
                'label_update',
                kwargs={'pk': self.label.id}
            )
        )  
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(
            response,
            f'{reverse("account_login")}?next=/labels/update/{self.label.id}/'
        )
        response = self.client.get(
            f'{reverse("account_login")}?next=/labels/update/{self.label.id}/'
        )
        self.assertContains(response, 'Log In')
        