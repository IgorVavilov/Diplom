# Generated by Django 4.1.7 on 2023-05-21 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="email",
            field=models.EmailField(blank=True, max_length=500, null=True, unique=True),
        ),
    ]