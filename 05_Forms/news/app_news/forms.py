import datetime
from django.core.exceptions import ValidationError
from app_news.models import User, News
from django import forms


class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = '__all__'


class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = '__all__'

    # class UserForm(forms.Form):
    # # username = forms.CharField(min_length=5, max_length=20)
    # # password = forms.CharField(min_length=5, max_length=20)
    # first_name = forms.CharField(max_length=20)
    # # second_name = forms.CharField(max_length=20)
    # last_name = forms.CharField(max_length=20)
    # # email = forms.EmailField()
    # birthday = forms.DateField()

    # def clean_birthday(self):
    #     data = self.cleaned_data['birthday']
    #     today = datetime.date.today()
    #     year_delta = (today - data).days / 365
    #     if year_delta < 18:
    #         raise ValidationError('Регистрироваться могут только лица старше 18 лет')
    #     return data
    #
    # def clean(self):
    #     clean_data = super(UserForm, self).clean()
    #     first_name = clean_data.get('first_name')
    #     last_name = clean_data.get('last_name')
    #     if first_name == 'Иван':
    #         msg = 'Запрещено регистрироваться, если ваше имя Иван!'
    #         self.add_error('first_name', msg)
    #     if last_name == 'Иванов':
    #         msg = 'Запрещено регистрироваться, если ваша фамилия Иванов!'
    #         self.add_error('last_name', msg)
    #
    #     # if first_name == 'Иван' and last_name == 'Иванов':
    #     #     raise ValidationError('Запрещено регистрироваться, если ваше имя и фамилия Иван Иванов!')
