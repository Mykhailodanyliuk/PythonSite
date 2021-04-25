import re
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django import forms


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label="Ім'я користувача", widget=forms.TextInput(attrs={'placeholder':"Ім'я користувача"}))
    password1 = forms.CharField(label="Пароль", widget=forms.PasswordInput(attrs={'placeholder':'Пароль'}))
    password2 = forms.CharField(label="Підтвердження пароля", widget=forms.PasswordInput(attrs={'placeholder':'Підтвердження пароля'}))
    email = forms.EmailField(label="Імейл", widget=forms.TextInput(attrs={'placeholder':'Імейл'}))

    class Meta:
        model = User
        fields = ('username','email','password1','password2')

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label="Ім'я користувача",
                               widget=forms.TextInput(attrs={'placeholder': "Ім'я користувача"}))
    password = forms.CharField(label="Пароль", widget=forms.PasswordInput(attrs={'placeholder': 'Пароль'}))