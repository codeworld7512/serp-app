# Generated by Django 4.2.5 on 2023-10-01 06:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Company",
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
                ("name", models.CharField(max_length=255)),
                ("url", models.URLField(blank=True, null=True)),
                ("slug", models.SlugField(unique=True)),
                ("logo", models.URLField()),
                ("description", models.TextField()),
                ("short_description", models.CharField(max_length=255)),
                ("one_liner_description", models.CharField(max_length=100)),
                ("address", models.CharField(max_length=255)),
                ("homepage_screenshot", models.URLField()),
                ("year_founded", models.PositiveIntegerField()),
                ("has_affiliate_program", models.BooleanField(default=False)),
                ("affiliate_signup_url", models.URLField(blank=True, null=True)),
                ("affiliate_login_url", models.URLField(blank=True, null=True)),
                (
                    "alternatives",
                    models.ManyToManyField(blank=True, to="website.company"),
                ),
            ],
        ),
        migrations.CreateModel(
            name="CompanyType",
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
                (
                    "company_type",
                    models.CharField(
                        choices=[
                            ("software", "Software"),
                            ("service provider", "Service Provider"),
                            ("local business", "Local Business"),
                            ("merchant account provider", "Merchant Account Provider"),
                        ],
                        max_length=255,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Pricing",
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
                ("price", models.DecimalField(decimal_places=2, max_digits=10)),
                ("has_free_plan", models.BooleanField(default=False)),
                ("has_free_trial", models.BooleanField(default=False)),
                ("is_open_source", models.BooleanField(default=False)),
                (
                    "pricing_model",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("monthly", "Monthly"),
                            ("yearly", "Yearly"),
                            ("one time", "One Time"),
                        ],
                        max_length=255,
                        null=True,
                    ),
                ),
                (
                    "company",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="pricing",
                        related_query_name="pricing",
                        to="website.company",
                    ),
                ),
            ],
            options={
                "verbose_name": "Pricing",
                "verbose_name_plural": "Pricing",
            },
        ),
        migrations.CreateModel(
            name="Feature",
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
                ("feature", models.CharField(max_length=255)),
                ("description", models.TextField(blank=True, null=True)),
                (
                    "company",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="features",
                        to="website.company",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="company",
            name="company_type",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="website.companytype"
            ),
        ),
    ]
