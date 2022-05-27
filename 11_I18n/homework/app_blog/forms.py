from django import forms
from .models import Blog
from django.utils.translation import gettext_lazy as _


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = '__all__'


class MultiFileForm(forms.Form):
    file_field = forms.FileField(label=_('Загрузка файлов'), widget=forms.ClearableFileInput(attrs={'multiple': True}),)


class UploadPriceForm(forms.Form):
    file = forms.FileField()
