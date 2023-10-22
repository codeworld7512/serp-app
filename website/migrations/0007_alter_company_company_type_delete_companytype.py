# Generated by Django 4.2.5 on 2023-10-01 12:55

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("website", "0006_company_article_alter_company_description_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="company",
            name="company_type",
            field=models.IntegerField(
                choices=[
                    (1, "Software"),
                    (2, "Service Provider"),
                    (3, "Local Business"),
                    (4, "Merchant Account Provider"),
                ]
            ),
        ),
        migrations.DeleteModel(
            name="CompanyType",
        ),
    ]
