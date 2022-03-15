from django.db import models


class News(models.Model):
    name = models.CharField(max_length=200, verbose_name='Название')
    content = models.CharField(max_length=2000, verbose_name='Содержание')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')
    published = models.BooleanField(default=False, verbose_name='Опубликован')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['created_at']


class Comment(models.Model):
    user_name = models.CharField(max_length=20, verbose_name='Имя пользователя')
    user_comment = models.CharField(max_length=2000, verbose_name='Комментарий')
    news = models.ForeignKey('News', default=None, on_delete=models.SET_NULL, null=True,
                             related_name='comments', verbose_name='Новости')

    def __str__(self):
        return f'Комментарий для новости: {self.news}'
