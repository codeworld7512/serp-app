# resources.py
from django.core.exceptions import ObjectDoesNotExist
from import_export import resources, fields
from .models import Company, CompanyCategory
from urllib.parse import quote

class CompanyResource(resources.ModelResource):
    id = fields.Field(attribute='id', column_name='company_id')
    article = fields.Field(attribute='article', column_name='company_article')
    homepage_screenshot = fields.Field(attribute='homepage_screenshot', column_name='homepage_screenshot')
    category_slugs = fields.Field(attribute='categories', column_name='category_slugs')
    
    class Meta:
        model = Company
        fields = (
            'id',
            'created_at',
            'name',
            'slug',
            'url',
            'serply_link',
            'logo',
            'description',
            'article',
            'short_description',
            'one_liner',
            'address',
            'homepage_screenshot',
            'year_founded',
            'has_affiliate_program',
            'affiliate_signup_url',
            'affiliate_login_url',
            'company_type',
            'categories',
            'alternatives'
        )
        import_id_fields = ('id',)
        skip_unchanged = True
        report_skipped = True
        exclude = ('id',)

    def before_import_row(self, row, **kwargs):
        homepage_screenshot = row.get("homepage_screenshot", "")
        encoded_homepage_screenshot = quote(homepage_screenshot, safe=":/")
        row["homepage_screenshot"] = encoded_homepage_screenshot
        
        # Handle categories
        category_slugs = row.get("category_slugs", "").split(",")  # using comma as a delimiter
        new_categories = []
        for slug in category_slugs:
            slug = slug.strip()  # remove leading and trailing whitespace
            try:
                category = CompanyCategory.objects.get(slug=slug)
                new_categories.append(category)
            except ObjectDoesNotExist:
                pass  # or you can create a new category here if desired
        
        # Only add new categories to row if the company already exists
        company_id = row.get("company_id", "")
        try:
            company = Company.objects.get(id=company_id)
            for category in new_categories:
                company.categories.add(category)  # add new categories to the existing ones
        except ObjectDoesNotExist:
            pass  # handle case where company does not exist


class CompanyCategoryResource(resources.ModelResource):
    category_id = fields.Field(attribute='id', column_name='category_id')

    class Meta:
        model = CompanyCategory
        fields = (
            'category_id',
            'created_at',
            'updated_at',
            'name',
            'slug',
            'description',
        )
        import_id_fields = ('category_id',)
        skip_unchanged = True
        report_skipped = True


