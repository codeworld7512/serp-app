# Generated by Django 4.2.3 on 2023-10-02 12:25

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("website", "0011_alter_company_options"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="companycategory",
            options={"ordering": ["name"], "verbose_name_plural": "Company Categories"},
        ),
        migrations.RenameField(
            model_name="companycategory",
            old_name="category",
            new_name="name",
        ),
        migrations.AlterField(
            model_name="company",
            name="alternatives",
            field=models.ManyToManyField(blank=True, to="website.company"),
        ),
        migrations.AlterField(
            model_name="company",
            name="categories",
            field=models.ManyToManyField(blank=True, to="website.companycategory"),
        ),
    ]
