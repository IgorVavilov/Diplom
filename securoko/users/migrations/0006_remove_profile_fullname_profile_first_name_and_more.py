# Generated by Django 4.1.7 on 2023-06-20 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0005_remove_profile_lastname_remove_profile_name_and_more"),
    ]

    operations = [
        migrations.RemoveField(model_name="profile", name="fullname",),
        migrations.AddField(
            model_name="profile",
            name="first_name",
            field=models.CharField(
                blank=True, max_length=200, null=True, verbose_name="Имя"
            ),
        ),
        migrations.AddField(
            model_name="profile",
            name="last_name",
            field=models.CharField(
                blank=True, max_length=200, null=True, verbose_name="Фамилия"
            ),
        ),
    ]
