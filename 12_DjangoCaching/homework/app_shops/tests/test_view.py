from django.test import TestCase
from django.urls import reverse


class TestView(TestCase):

    def test_main(self):
        url = reverse('main')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Это главная страница!')

    def test_account(self):
        url = reverse('account')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 403)


