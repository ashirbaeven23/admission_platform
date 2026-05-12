from django import forms

from django.contrib.auth.forms import (
    AuthenticationForm,
    UserCreationForm,
)

from .models import User


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'w-full bg-slate-100 rounded-2xl px-6 py-5 outline-none',
                'placeholder': 'Логин'
            }
        )
    )

    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'w-full bg-slate-100 rounded-2xl px-6 py-5 outline-none',
                'placeholder': 'Пароль'
            }
        )
    )


class RegisterForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'w-full bg-slate-100 rounded-2xl px-6 py-5 outline-none',
                'placeholder': 'Логин'
            }
        )
    )

    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                'class': 'w-full bg-slate-100 rounded-2xl px-6 py-5 outline-none',
                'placeholder': 'Email'
            }
        )
    )

    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'w-full bg-slate-100 rounded-2xl px-6 py-5 outline-none',
                'placeholder': 'Пароль'
            }
        )
    )

    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'w-full bg-slate-100 rounded-2xl px-6 py-5 outline-none',
                'placeholder': 'Подтвердите пароль'
            }
        )
    )

    class Meta:
        model = User

        fields = (
            'username',
            'email',
            'password1',
            'password2',
        )