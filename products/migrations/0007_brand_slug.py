# Generated by Django 4.1.3 on 2023-02-24 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0006_productimage"),
    ]

    operations = [
        migrations.AddField(
            model_name="brand",
            name="slug",
            field=models.SlugField(blank=True, null=True),
        ),
    ]