from django.db import models


class User(models.Model):
    # username = models.CharField(max_length=20)
    # password = models.CharField(max_length=20)
    first_name = models.CharField(max_length=20)
    # second_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    # email = models.EmailField()
    birthday = models.DateField()

    def __str__(self):
        return self.first_name


class News(models.Model):
    name = models.CharField(max_length=200, verbose_name='Название')
    content = models.CharField(max_length=2000, verbose_name='Содержание')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')
    published = models.BooleanField(default=False, verbose_name='Опубликован')
    # comments = models.ForeignKey('Comment', default=None, on_delete=models.SET_NULL, null=True,
    #                          verbose_name='Комментарии')

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
