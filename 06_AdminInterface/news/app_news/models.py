from django.db import models


class News(models.Model):
    STATUS_CHOICES = [
        ('p', 'Опубликован'),
        ('n', 'Неопубликован'),
    ]
    name = models.CharField(max_length=200, verbose_name='Название')
    content = models.CharField(max_length=2000, verbose_name='Содержание')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='n', verbose_name='Статус')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['created_at']


class Comment(models.Model):
    STATUS_CHOICES = [
        ('a', 'Активен'),
        ('d', 'Удалено Администратором'),
    ]
    user_name = models.CharField(max_length=20, verbose_name='Имя пользователя')
    user_comment = models.CharField(max_length=2000, verbose_name='Комментарий')
    news = models.ForeignKey('News', default=None, on_delete=models.SET_NULL, null=True,
                             related_name='comments', verbose_name='Новости')
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='a', verbose_name='Статус')

    def comment(self):
        return f'{self.user_comment[:15]}...'

    comment.short_description = 'Комментарий'

    def __str__(self):
        return f'Комментарий для новости: {self.news}'
