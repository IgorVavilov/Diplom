from django.forms import ModelForm
from .models import ContactMessage
from django import forms


class ContactForm(ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['sender_name', 'sender_email', 'sender_subject', 'sender_message']
        labels = {'sender_name': 'ФИО:',
                  'sender_email': 'E-mail:',
                  'sender_subject': 'Тема:',
                  'sender_message': 'Сообщение:'}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input_field'})