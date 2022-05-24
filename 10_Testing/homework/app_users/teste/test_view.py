from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User


class TestView(TestCase):

    def test_login(self):
        url = reverse('login')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Страница входа')

    def test_logout(self):
        url = reverse('logout')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)

    def test_register(self):
        url = reverse('register')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name='users/register.html')

    def test_user_edit(self):
        User.objects.create()
        url = '/user/1/edit'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 403)
