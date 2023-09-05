from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from .models import CustomUser


class Login_form(AuthenticationForm):
    class Meta:
        model = CustomUser
        fields = [
            "email"
        ]
        widgets = {
            "password": forms.PasswordInput()
        }


class Signup_form(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = [
            'email',
            'password'
        ]
