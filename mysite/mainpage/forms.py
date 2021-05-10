from .models import Products
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from django.forms import ModelForm,TextInput
from django.utils import timezone



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

class ProductsForm(ModelForm):
    name_product = forms.CharField(label=False,widget=forms.TextInput(attrs={'placeholder': "Назва"}))
    price_product = forms.IntegerField(label=False, widget=forms.NumberInput(attrs={'placeholder': "Ціна"}))
    about_product = forms.CharField(label=False, widget=forms.Textarea(attrs={'placeholder': "Про товар"}))


    class Meta:
        model = Products
        fields = ['name_product','price_product','about_product']

        # widgets = {
        #     "name_product" : TextInput(attrs={
        #         'type': 'text',
        #         'placeholder': 'Назва'
        #     })
        # }
