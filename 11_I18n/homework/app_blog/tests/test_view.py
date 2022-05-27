from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from app_blog.models import Blog, Profile


class TestView(TestCase):

    def test_main(self):
        url = reverse('main')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Это главная страница!')

    def test_url_blog_upload(self):
        url = reverse('blog_upload')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Загрузить блог(и)')

    def test_blog_detail(self):
        User.objects.create()
        Profile.objects.create(user_id=1)
        Blog.objects.create(article='test', created_at='10/10/2010')
        url = '/blog/1'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'blog-detail')

    def test_url_img_upload(self):
        url = reverse('img_upload')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 403)
