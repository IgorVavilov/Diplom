from django.contrib import admin
from .models import *


class ProfileAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'first_name', 'last_name', 'profile_image', 'created']


class ProfileContactMessage(admin.ModelAdmin):
    list_display = ['sender', 'recipient', 'name', 'sender_email', 'sender_subject', 'is_read', 'created']


admin.site.register(Profile, ProfileAdmin)
admin.site.register(ContactMessage, ProfileContactMessage)

