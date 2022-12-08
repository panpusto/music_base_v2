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
            added_by_id=cls.user.id
        )

    def test_label_listing(self):
        self.assertEqual(f'{self.label.name}', '2020') 

    def test_add_label_view_for_logged_in_user(self):
        self.client.login(email='testuser1@email.com', password='testpass123')
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
            response, '%s?next=/labels/add/' % (reverse('account_login'))
        )
        response = self.client.get(
            '%s?next=/labels/add/' % (reverse('account_login'))
        )   
        self.assertContains(response, 'Log In')

        # TODO add test for detail view
