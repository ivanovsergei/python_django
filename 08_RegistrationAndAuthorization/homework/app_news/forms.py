from django import forms
from django.forms import Textarea
from .models import News, Comment


class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = '__all__'


class CommentFormIsAuth(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('user_comment',)
        widgets = {'user_comment': Textarea(attrs={'cols': 35, 'rows': 5})}


class CommentFormNotIsAuth(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('not_auth_user_name', 'user_comment')
        widgets = {
            'user_comment': Textarea(attrs={'cols': 30, 'rows': 5})
            }
