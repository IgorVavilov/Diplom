# Generated by Django 4.1.7 on 2023-07-05 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0012_profile_phone_number"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="phone_number",
            field=models.CharField(
                blank=True, default="", max_length=50, null=True, verbose_name="Телефон"
            ),
        ),
    ]
