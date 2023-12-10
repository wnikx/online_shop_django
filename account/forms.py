from django import forms
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    username = forms.CharField(label="Логин:")
    password = forms.CharField(widget=forms.PasswordInput, label="Пароль: ")


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Пароль: ', widget=forms.PasswordInput)
    password_2 = forms.CharField(
        label='Повторите пароль: ', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'email']

    def clean_password_2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password_2']:
            return forms.ValidationError('Пароли не совпдают')
        return cd['password_2']
