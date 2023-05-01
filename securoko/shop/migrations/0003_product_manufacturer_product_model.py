# Generated by Django 4.1.7 on 2023-05-01 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("shop", "0002_rename_description_product_short_description_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="manufacturer",
            field=models.CharField(db_index=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name="product",
            name="model",
            field=models.CharField(db_index=True, max_length=200, null=True),
        ),
    ]
