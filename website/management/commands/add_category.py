from django.core.management.base import BaseCommand
from website.models import Company, CompanyCategory
from django.db.utils import IntegrityError

class Command(BaseCommand):
    help = 'Add a CompanyCategory to each Company in the database'

    def handle(self, *args, **options):
        category_name = 'Artificial Intelligence Tools'
        
        # Try to create the category, skip if already exists
        try:
            category, created = CompanyCategory.objects.get_or_create(
                category=category_name,
                defaults={'slug': 'artificial-intelligence-tools'},
            )
        except IntegrityError:
            self.stdout.write(self.style.ERROR(f'Category "{category_name}" already exists.'))
            return

        if created:
            self.stdout.write(self.style.SUCCESS(f'Successfully created category "{category_name}".'))
        else:
            self.stdout.write(self.style.SUCCESS(f'Category "{category_name}" already exists.'))

        # Add category to all companies
        for company in Company.objects.all():
            company.categories.add(category)
            self.stdout.write(self.style.SUCCESS(f'Added category "{category_name}" to company "{company.name}".'))
