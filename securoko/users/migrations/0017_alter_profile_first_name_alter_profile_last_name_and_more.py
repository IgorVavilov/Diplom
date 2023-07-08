# Generated by Django 4.1.7 on 2023-07-08 04:45

from django.db import migrations, models
import phonenumber_field.modelfields
import shop.utils


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0016_alter_profile_phone_number"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="first_name",
            field=models.CharField(
                blank=True,
                max_length=20,
                null=True,
                validators=[shop.utils.validate_name],
                verbose_name="Имя",
            ),
        ),
        migrations.AlterField(
            model_name="profile",
            name="last_name",
            field=models.CharField(
                blank=True,
                max_length=30,
                null=True,
                validators=[shop.utils.validate_name],
                verbose_name="Фамилия",
            ),
        ),
        migrations.AlterField(
            model_name="profile",
            name="phone_number",
            field=phonenumber_field.modelfields.PhoneNumberField(
                blank=True,
                default="",
                max_length=20,
                null=True,
                region="RU",
                verbose_name="Телефон",
            ),
        ),
        migrations.AlterField(
            model_name="profile",
            name="username",
            field=models.CharField(
                blank=True, max_length=30, null=True, verbose_name="Имя пользователя"
            ),
        ),
    ]
