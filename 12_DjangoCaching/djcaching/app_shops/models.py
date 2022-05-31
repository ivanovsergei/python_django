from django.contrib.auth.models import User
from django.db import models


class Client(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')

    def __str__(self):
        return self.user.username


class Shop(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название магазина')


class Promotion(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название акции')
    user = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='promotions')


class Balance(models.Model):
    balance = models.IntegerField(default=100)


class Offers(models.Model):
    title = models.CharField(max_length=100, verbose_name='Предложения')


class PaymentHistory(models.Model):
    good = models.CharField(max_length=100, verbose_name='Товар')
    price = models.IntegerField(default='')
