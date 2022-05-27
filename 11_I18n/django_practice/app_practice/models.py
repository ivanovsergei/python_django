from django.db import models
from django.utils.translation import gettext_lazy as _


class Users(models.Model):
    user = models.CharField(max_length=30, verbose_name=_('user'))

    def __str__(self):
        return self.user

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
