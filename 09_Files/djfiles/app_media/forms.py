from django import forms
from .models import File


class ExUploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    description = forms.CharField(max_length=100)
    file = forms.FileField()


class UploadPriceForm(forms.Form):
    file = forms.FileField()


class ModelUploadForm(forms.ModelForm):
    class Meta:
        model = File
        fields = ('description', 'file')


class MultiFileForm(forms.Form):
    file_field = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
