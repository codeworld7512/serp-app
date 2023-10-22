# website/models.py

from django.db import models

class Company(models.Model):
    """
    Model representing a company.
    """
    created_at = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    url = models.URLField(blank=True, null=True)
    serply_link = models.URLField(blank=True, null=True)
    logo = models.URLField(blank=True, null=True)
    one_liner = models.CharField(max_length=100,blank=True, null=True)
    short_description = models.CharField(max_length=255,blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    article = models.TextField(blank=True, null=True)
    address = models.CharField(max_length=255,blank=True, null=True)
    homepage_screenshot = models.URLField(blank=True, null=True)
    YEAR_CHOICES = [
        (str(year), str(year)) for year in range(1900, 2101)
        ]
    year_founded = models.IntegerField(blank=True, null=True, choices=YEAR_CHOICES)
    has_affiliate_program = models.BooleanField(default=False,blank=True, null=True)
    affiliate_signup_url = models.URLField(null=True, blank=True)
    affiliate_login_url = models.URLField(null=True, blank=True)
    COMPANY_TYPE_CHOICES = [
        (1, 'Software'),
        (2, 'Service Provider'),
        (3, 'Local Business'),
        (4, 'Merchant Account Provider'),
    ]
    company_type = models.IntegerField(
        choices=COMPANY_TYPE_CHOICES,
    )
    categories = models.ManyToManyField('CompanyCategory', blank=True)
    alternatives = models.ManyToManyField('self', symmetrical=True, blank=True,)

    class Meta:
        ordering = ['name']
        verbose_name_plural = 'Companies'

    def __str__(self):
        return self.name

class CompanyCategory(models.Model):
    """
    Model representing a company category.
    """
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)  
    name = models.CharField(max_length=255, unique=True)  
    slug = models.SlugField(unique=True)  
    description = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        ordering = ['name']
        verbose_name_plural = 'Company Categories'

    def __str__(self):
        return self.name


class Feature(models.Model):
    """
    Model representing a feature.
    """
    created_at = models.DateTimeField(auto_now_add=True)
    feature = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    company = models.ForeignKey(Company, related_name='features', on_delete=models.CASCADE)

    def __str__(self):
        return self.feature


class Pricing(models.Model):
    """
    Model representing the pricing information for a company.
    """
    created_at = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    has_free_plan = models.BooleanField(null=True, blank=True, default=None)
    has_free_trial = models.BooleanField(null=True, blank=True, default=None)
    is_open_source = models.BooleanField(null=True, blank=True, default=None)
    PRICING_MODEL_CHOICES = [
        ('monthly', 'Monthly'),
        ('yearly', 'Yearly'),
        ('one time', 'One Time'),
    ]
    pricing_model = models.IntegerField(
        choices=PRICING_MODEL_CHOICES,
        blank=True,
        null=True,
    )
    company = models.ForeignKey(Company, related_name='pricing', related_query_name='pricing', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Pricing'
        verbose_name_plural = 'Pricing'

    def __str__(self):
        return self.pricing_model
    
    company = models.ForeignKey(Company, related_name='pricing', related_query_name='pricing', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Pricing'
        verbose_name_plural = 'Pricing'

    def __str__(self):
        return self.pricing_model