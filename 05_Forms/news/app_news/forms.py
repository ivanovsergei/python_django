import datetime
from django.core.exceptions import ValidationError
from app_news.models import News
from django import forms


class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = '__all__'

