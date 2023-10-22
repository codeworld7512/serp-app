# Generated by Django 4.2.5 on 2023-10-01 13:52

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("website", "0008_alter_company_address_alter_company_alternatives_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="pricing",
            name="has_free_plan",
            field=models.BooleanField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name="pricing",
            name="has_free_trial",
            field=models.BooleanField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name="pricing",
            name="is_open_source",
            field=models.BooleanField(blank=True, default=None, null=True),
        ),
    ]
