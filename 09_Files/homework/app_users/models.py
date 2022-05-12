from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30, default='', verbose_name='Имя')
    last_name = models.CharField(max_length=30, default='', verbose_name='Фамилия')
    description = models.CharField(max_length=1000, default='', verbose_name='О себе')
    city = models.CharField(max_length=36, blank=True)

    def __str__(self):
        return self.user.username
