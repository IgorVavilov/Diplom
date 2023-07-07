from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _
import re


def validate_name(value):
    if not value.isalpha():
        raise ValidationError(
            _("Неверное значение: %(value)s. Поле должно содержать только буквы."),
            params={"value": value},
        )


# RE = re.compile('[Я-а]')


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Имя пользователя')
    email = models.EmailField(max_length=500, unique=True, null=True, blank=True)
    phone_number = PhoneNumberField('Телефон', max_length=20, default='', null=True, blank=True, region='RU')
    first_name = models.CharField(max_length=20, verbose_name='Имя', null=True, blank=True,
                                  validators=[validate_name],)
    last_name = models.CharField(max_length=30, null=True, blank=True, verbose_name='Фамилия',
                                  validators=[validate_name],)
    username = models.CharField(max_length=30, null=True, blank=True, verbose_name='Имя пользователя')
    profile_image = models.ImageField(upload_to='profiles/', default='profile/user-default.png', verbose_name='Фото профиля')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    def __str__(self):
        return f"{self.username}"

    class Meta:
        ordering = ('-created',)
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'


class ContactMessage(models.Model):
    sender = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True, blank=True)
    recipient = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True, blank=True, related_name='messages')
    name = models.CharField(max_length=200, null=True, blank=True)
    sender_email = models.EmailField(max_length=500)
    sender_subject = models.CharField(max_length=250)
    sender_message = models.TextField(null=True, blank=True)
    is_read = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.sender_subject

    class Meta:
        ordering = ('-created',)
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'

