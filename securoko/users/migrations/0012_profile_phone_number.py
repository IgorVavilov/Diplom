# Generated by Django 4.1.7 on 2023-07-05 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0011_alter_contactmessage_options_alter_profile_options"),
    ]

    operations = [
        migrations.AddField(
            model_name="profile",
            name="phone_number",
            field=models.CharField(default="", max_length=50, verbose_name="Телефон"),
        ),
    ]
