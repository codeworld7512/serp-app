# Generated by Django 4.2.5 on 2023-10-01 19:59

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("website", "0009_alter_pricing_has_free_plan_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="company",
            old_name="one_liner_description",
            new_name="one_liner",
        ),
    ]