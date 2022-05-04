from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    city = models.CharField(max_length=36, blank=True)
    telephone = models.CharField(max_length=30, blank=True)
    verification = models.BooleanField(default=True)
    count_published_news = models.IntegerField(default=0)

    class Meta:
        permissions = (
            ("can verify", "может верифицировать"),
        )

    def __str__(self):
        return self.user.username
