from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30, default='', verbose_name=_('Имя'))
    last_name = models.CharField(max_length=30, default='', verbose_name=_('Фамилия'))
    description = models.CharField(max_length=1000, default='', verbose_name=_('О себе'))
    city = models.CharField(max_length=36, blank=True, verbose_name=_('Город'))

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = _('профиль')
        verbose_name_plural = _('профили')
