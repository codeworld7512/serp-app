# Generated by Django 4.2.5 on 2023-10-01 09:01

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("website", "0003_companycategory_company_categories"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="companycategory",
            options={
                "ordering": ["category"],
                "verbose_name_plural": "Company Categories",
            },
        ),
        migrations.AddField(
            model_name="companycategory",
            name="slug",
            field=models.SlugField(default="NULL", unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="companycategory",
            name="updated_at",
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name="company",
            name="address",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name="company",
            name="description",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="company",
            name="homepage_screenshot",
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="company",
            name="logo",
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="company",
            name="short_description",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name="company",
            name="year_founded",
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="companycategory",
            name="category",
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name="pricing",
            name="has_free_plan",
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name="pricing",
            name="has_free_trial",
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name="pricing",
            name="is_open_source",
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
