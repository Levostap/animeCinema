from django.urls import path

from cards.views import catalog

app_name = "catalog"

urlpatterns = [
    path('', catalog, name='catalog'),
]

