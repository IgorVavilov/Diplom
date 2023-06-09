# Generated by Django 4.1.7 on 2023-06-20 15:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0006_remove_profile_fullname_profile_first_name_and_more"),
        ("orders", "0005_alter_order_owner"),
    ]

    operations = [
        migrations.AlterField(
            model_name="order",
            name="owner",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="users.profile",
            ),
        ),
    ]
