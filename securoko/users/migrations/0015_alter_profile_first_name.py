# Generated by Django 4.1.7 on 2023-07-07 15:44

from django.db import migrations, models
import users.models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0014_alter_profile_first_name_alter_profile_phone_number"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="first_name",
            field=models.CharField(
                blank=True,
                max_length=200,
                null=True,
                validators=[users.models.validate_name],
                verbose_name="Имя",
            ),
        ),
    ]
