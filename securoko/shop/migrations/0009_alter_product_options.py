# Generated by Django 4.1.7 on 2023-07-05 16:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("shop", "0008_delete_contactmessage"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="product",
            options={
                "ordering": ("name",),
                "verbose_name": "Товар",
                "verbose_name_plural": "Товары",
            },
        ),
    ]
