from django.forms import Textarea

from .models import News, Comment
from django import forms


class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = '__all__'


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = '__all__'
        widgets = {'user_comment': Textarea(attrs={'cols': 30, 'rows': 5})}
