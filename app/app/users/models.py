from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    images = models.ImageField(upload_to='main/images', blank=True, null=True, verbose_name="Аватар")
    age = models.PositiveSmallIntegerField(blank=True, null=True, verbose_name="Возраст")
    class Meta:
        db_table = 'user'
        verbose_name = "Пользователя"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.username