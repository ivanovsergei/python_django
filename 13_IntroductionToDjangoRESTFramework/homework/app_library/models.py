from django.db import models


class Author(models.Model):
    first_name = models.CharField(max_length=30, verbose_name='Имя')
    last_name = models.CharField(max_length=50, verbose_name='Фамилия')
    birthday = models.DateField()

    def __str__(self):
        return self.last_name

    class Meta:
        ordering = ['id']


class Book(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название книги')
    isbn = models.IntegerField()
    published_at = models.DateField(verbose_name='Год выпуска')
    page_count = models.IntegerField(verbose_name='Количество страниц')
    author = models.ForeignKey(Author, on_delete=models.CASCADE,
                               default=None, null=True, verbose_name='Автор')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['id']
