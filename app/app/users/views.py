from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from users.forms import UserLoginForm, UserRegistrationForm


# Create your views here.
class LoginUser(LoginView):
    form_class = UserLoginForm
    template_name = "users/login.html"
    extra_context = {"title": "Авторизация"}

class RegisterUser(CreateView):
    form_class = UserRegistrationForm
    template_name = "users/register.html"
    extra_context = {"title": "Регистрация"}
    success_url = reverse_lazy("user:login")


def profile(request): ...
