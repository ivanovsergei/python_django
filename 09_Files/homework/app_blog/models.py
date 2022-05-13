from django.db import models
from app_users.models import Profile


class Blog(models.Model):

    title = models.CharField(max_length=200, verbose_name='Название')
    username = models.ForeignKey(Profile, on_delete=models.CASCADE, verbose_name='Профиль пользователя')
    article = models.TextField(max_length=2000, verbose_name='Содержание статьи')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'статья'
        verbose_name_plural = 'статьи'

    def __str__(self):
        return f'{self.article[:100]}...'


class File(models.Model):
    file = models.FileField(upload_to='files/')
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['id']
        verbose_name = 'файл'
        verbose_name_plural = 'файлы'
