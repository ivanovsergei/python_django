from django.db import models
from app_users.models import Profile


class Blog(models.Model):

    title = models.CharField(max_length=200, blank=True, verbose_name='Название')
    username = models.ForeignKey(Profile, on_delete=models.CASCADE, default=1, verbose_name='Автор статьи')
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
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, verbose_name='Файлы к статье', related_name='blog')
    file = models.FileField(upload_to='files/')
    filename = models.CharField(max_length=30, verbose_name='Название файла')
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['id']
        verbose_name = 'файл'
        verbose_name_plural = 'файлы'

    def __str__(self):
        return self.file.name