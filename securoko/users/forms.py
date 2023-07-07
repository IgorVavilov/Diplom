from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import Profile
from .models import ContactMessage
from django import forms
from django.contrib import messages
import phonenumbers


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input_field_form'})


class ProfileForm(ModelForm):
    # phone_number = PhoneNumberField(region='RU', blank=True, null=True)

    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'username', 'profile_image']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.fields['first_name'].error_messages['required'] = 'Это поле обязательно'

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input_field_form'})

    # def clean_phone_number(self):
    #     phone_number = self.cleaned_data.get("phone_number")
    #     z = phonenumbers.parse(phone_number, "RU")
    #     if not phonenumbers.is_valid_number(z):
    #         raise forms.ValidationError("Number not in RU format")
    #     return phone_number


class ContactForm(ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'sender_email', 'sender_subject', 'sender_message']
        labels = {'name': 'ФИО:',
                  'sender_email': 'E-mail:',
                  'sender_subject': 'Тема:',
                  'sender_message': 'Сообщение:'}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input_field'})