from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Имя пользователя')
    email = models.EmailField(max_length=500, unique=True, null=True, blank=True)
    first_name = models.CharField(max_length=200, null=True, blank=True, verbose_name='Имя')
    last_name = models.CharField(max_length=200, null=True, blank=True, verbose_name='Фамилия')
    username = models.CharField(max_length=200, null=True, blank=True, verbose_name='Имя пользователя')
    profile_image = models.ImageField(upload_to='profiles/', default='profile/user-default.png', verbose_name='Фото профиля')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    def __str__(self):
        return f"{self.username}"


