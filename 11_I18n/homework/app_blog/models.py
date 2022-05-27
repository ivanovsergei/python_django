from django.db import models
from app_users.models import Profile
from django.utils.translation import gettext_lazy as _


class Blog(models.Model):

    title = models.CharField(max_length=200, blank=True, verbose_name=_('Название'))
    username = models.ForeignKey(Profile, on_delete=models.CASCADE, default=1, verbose_name=_('Автор статьи'))
    article = models.TextField(max_length=2000, verbose_name=_('Содержание статьи'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Дата создания'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('Дата обновления'))

    class Meta:
        ordering = ['-created_at']
        verbose_name = _('статья')
        verbose_name_plural = _('статьи')

    def __str__(self):
        return f'{self.article[:100]}...'


class File(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, verbose_name=_('Файлы к статье'), related_name='blog')
    file = models.FileField(upload_to='files/')
    filename = models.CharField(max_length=30, verbose_name=_('Название файла'))
    description = models.TextField(blank=True, verbose_name=_('Описание'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Дата создания'))

    class Meta:
        ordering = ['id']
        verbose_name = _('файл')
        verbose_name_plural = _('файлы')

    def __str__(self):
        return self.file.name
