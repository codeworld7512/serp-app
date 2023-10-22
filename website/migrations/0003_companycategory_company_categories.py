# Generated by Django 4.2.5 on 2023-10-01 06:48

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("website", "0002_company_serply_link"),
    ]

    operations = [
        migrations.CreateModel(
            name="CompanyCategory",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("category", models.CharField(max_length=255)),
                (
                    "description",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
            ],
        ),
        migrations.AddField(
            model_name="company",
            name="categories",
            field=models.ManyToManyField(blank=True, to="website.companycategory"),
        ),
    ]