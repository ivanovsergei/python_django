from django import forms
from .models import Account


class BalanceForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ['balance']
