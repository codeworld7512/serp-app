# Generated by Django 4.2.5 on 2023-10-01 06:35

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("website", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="company",
            name="serply_link",
            field=models.URLField(blank=True, null=True),
        ),
    ]