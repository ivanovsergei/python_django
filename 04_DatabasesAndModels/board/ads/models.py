from django.db import models


class Advertisement(models.Model):
    title = models.CharField(max_length=1000, db_index=True, verbose_name='Заголовок')
    description = models.CharField(max_length=1000, default='', verbose_name='Описание')
    created_at = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')
    closed_at = models.DateTimeField(auto_now=True, verbose_name='Дата окончания публикации.')
    price = models.FloatField(verbose_name='цена', default=0)
    views_count = models.IntegerField(verbose_name='количество просмотров', default=0)
    status = models.ForeignKey('AdvertisementStatus', default=None, null=True, on_delete=models.CASCADE,
                               related_name='advertisements', verbose_name='Статус')
    author = models.ForeignKey('AdvertisementAuthor', default=None, null=True, on_delete=models.CASCADE,
                               verbose_name='Автор')
    categories = models.ForeignKey('AdvertisementCategories', default=None, null=True, on_delete=models.CASCADE,
                                   verbose_name='Категории')

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'ads_advertisement'
        ordering = ['title']


class AdvertisementStatus(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class AdvertisementAuthor(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class AdvertisementCategories(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
