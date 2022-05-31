from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _


class Client(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_('Пользователь'))

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = _('покупатель')
        verbose_name_plural = _('покупатели')


class Shop(models.Model):
    name = models.CharField(max_length=50, verbose_name=_('Название магазина'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('магазин')
        verbose_name_plural = _('магазины')


class Promotion(models.Model):
    title = models.CharField(max_length=100, verbose_name=_('Название акции'))
    user = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='promotions', verbose_name=_('Пользователь'))

    class Meta:
        verbose_name = _('промо акция')
        verbose_name_plural = _('промо акции')


class Balance(models.Model):
    amount = models.IntegerField(default=100, null=True, blank=True, verbose_name=_('Сумма'))
    user = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='balance', verbose_name=_('Пользователь'))

    class Meta:
        verbose_name = _('баланс')
        verbose_name_plural = _('баланс')


class Offers(models.Model):
    title = models.CharField(max_length=100, verbose_name=_('Предложения'))
    user = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='offers', verbose_name=_('Пользователь'))

    class Meta:
        verbose_name = _('предложение')
        verbose_name_plural = _('предложения')


class PaymentHistory(models.Model):
    good = models.CharField(max_length=100, verbose_name=_('Товар'))
    price = models.IntegerField(default='', null=True, verbose_name=_('Цена'))
    user = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='payment_history',
                             verbose_name=_('Пользователь'))

    class Meta:
        verbose_name = _('история покупок')
        verbose_name_plural = _('история покупок')
