from django.contrib.auth.views import LogoutView
from django.urls import path
from users.views import *

app_name = 'user'

urlpatterns = [
    path('login/', LoginUser.as_view(), name='login'),
    path('registration/', RegisterUser.as_view(), name='registration'),
    path('profile/', profile, name='profile'),
    path('logout/', LogoutView.as_view(), name='logout'),
]