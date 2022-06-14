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
    name = models.CharField(max_length=200, verbose_name='название')
    description = models.TextField(blank=True, verbose_name='описание')
    shops = models.ManyToManyField(Shop, related_name='goods', verbose_name='магазины')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-id']
        verbose_name = 'товар'
        verbose_name_plural = 'товары'


class Account(models.Model):
    STATUS_CHOICES = [
        ('n', 'начальный'),
        ('a', 'средний'),
        ('h', 'высокий'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='пользователь')
    balance = models.PositiveIntegerField(default=0, verbose_name='баланс')
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='n', verbose_name='статус')

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = 'аккаунт'
        verbose_name_plural = 'аккаунты'
