from django.contrib import admin
from .models import Profile


class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'name', 'email', 'username', 'profile_image', 'created']

admin.site.register(Profile, ProfileAdmin)

