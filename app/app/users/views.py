from django.shortcuts import render

# Create your views here.
def login(request):
    prev_page_url = request.META.get('HTTP_REFERER')
    context = {
        "title": "Авторизация",
        "prev_page": prev_page_url,
    }
    return render(request, "users/login.html", context=context)

def registration(request):
    prev_page_url = request.META.get('HTTP_REFERER')
    context = {
        "title": "Регистрация",
        "prev_page": prev_page_url,
    }
    return render(request, "users/register.html", context=context)

def profile(request): ...

def logout(request): ...
