# Generated by Django 4.1.7 on 2023-06-25 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("shop", "0005_categoryarticle_article"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="slug",
            field=models.SlugField(max_length=200, unique=True),
        ),
    ]
