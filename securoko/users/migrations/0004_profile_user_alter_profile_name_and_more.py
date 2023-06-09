# Generated by Django 4.1.7 on 2023-05-29 15:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("users", "0003_remove_profile_user_profile_lastname_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="profile",
            name="user",
            field=models.OneToOneField(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
                verbose_name="Имя пользователя",
            ),
        ),
        migrations.AlterField(
            model_name="profile",
            name="name",
            field=models.CharField(
                blank=True, max_length=200, null=True, verbose_name="Имя"
            ),
        ),
        migrations.AlterField(
            model_name="profile",
            name="username",
            field=models.CharField(
                blank=True, max_length=200, null=True, verbose_name="Имя пользователя"
            ),
        ),
    ]
