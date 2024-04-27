from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


User = get_user_model()


class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = (
            "username",
            "email",
            "password1",
            "password2",
        )

    username = forms.CharField()
    email = forms.CharField()
    password1 = forms.CharField()
    password2 = forms.CharField()


class UserLoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']

    username = forms.CharField()
    password = forms.CharField()


