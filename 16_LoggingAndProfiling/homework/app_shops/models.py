from django.db import models
from django.contrib.auth.models import User


class Shop(models.Model):
    name = models.CharField(max_length=50, verbose_name='название магазина')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'магазин'
        verbose_name_plural = 'магазины'


class Good(models.Model):
    name = models.CharField(max_length=200, db_index=True, verbose_name='название')
    slug = models.SlugField(max_length=200, db_index=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='цена')
    shops = models.ManyToManyField(Shop, related_name='goods', verbose_name='магазины')
    stock = models.PositiveIntegerField(verbose_name='остаток товара')
    top_sell = models.PositiveIntegerField(verbose_name='количество продаж')
    created = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-id']
        verbose_name = 'товар'
        verbose_name_plural = 'товары'
        index_together = (('id', 'slug'),)


class Account(models.Model):
    STATUS_CHOICES = [
        ('n', 'начальный'),
        ('a', 'средний'),
        ('h', 'высокий'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='пользователь')
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name='баланс')
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='n', verbose_name='статус')
    spend_money = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name='потрачено денег')

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = 'аккаунт'
        verbose_name_plural = 'аккаунты'
