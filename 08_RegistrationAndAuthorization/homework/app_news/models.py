from django.db import models
from app_users.models import Profile


class News(models.Model):

    title = models.CharField(max_length=200, verbose_name='Название')
    content = models.TextField(max_length=2000, verbose_name='Содержание')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')
    tags = models.CharField(max_length=200, null=True, verbose_name='Тег')

    class Meta:
        ordering = ['created_at']
        verbose_name = 'новость'
        verbose_name_plural = 'новости'
        permissions = (
            ("can publish", "может публиковать"),
        )

    def __str__(self):
        return self.title


class Comment(models.Model):
    user_name = models.ForeignKey(Profile, on_delete=models.CASCADE, verbose_name='Профиль пользователя')
    not_auth_user_name = models.CharField(max_length=30, default=None, null=True, verbose_name='Имя пользователя')
    user_comment = models.CharField(max_length=2000, null=True, blank=True, verbose_name='Комментарий')
    news = models.ForeignKey('News', default=None, on_delete=models.SET_NULL, null=True,
                             related_name='comments', verbose_name='Новости')

