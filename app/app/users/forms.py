from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordChangeForm
from django.core.exceptions import ValidationError


class UserLoginForm(AuthenticationForm):
    username = forms.CharField()
    password = forms.CharField()
    class Meta:
        model = get_user_model()
        fields = ["username", "password"]

class UserRegistrationForm(UserCreationForm):
    username = forms.CharField()
    email = forms.CharField()
    first_name = forms.CharField()
    last_name = forms.CharField()
    age = forms.CharField()
    password1 = forms.CharField()
    password2 = forms.CharField()

    class Meta:
        model = get_user_model()
        fields = ["first_name", "last_name", "age", "email", "username", "password1", "password2"]

    def clean_email(self):
        email = self.cleaned_data["email"]
        if get_user_model().objects.filter(email=email).exists():
            raise ValidationError("Такой email уже зарегистрирован")
        return email