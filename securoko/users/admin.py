from django.contrib import admin
from .models import Profile


class ProfileAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'fullname', 'profile_image', 'created']

admin.site.register(Profile, ProfileAdmin)

