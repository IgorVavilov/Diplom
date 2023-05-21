from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    email = models.EmailField(max_length=500, null=True, blank=True)
    username = models.CharField(max_length=200, null=True, blank=True)
    profile_image = models.ImageField(upload_to='profiles/', default='profile/user-default.png')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.username}"