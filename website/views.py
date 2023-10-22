# website/views.py

import os
from django.core.cache import cache
from django.http import Http404, HttpResponse
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, render, reverse
from .models import Company, CompanyCategory

from utils import conditional_cache_page, paginate_queryset


# ------------------------------
# ------------------------------
# region URL VIEWS


# --------------------
# region CORE

@conditional_cache_page(60 * 60 * 24 * 365, key_prefix="index", condition=not os.getenv("DEBUG"))
def index(request):
    """
    View function for the index page.
    """
    
    template = "website/index.html"

    items = Company.objects.all()
    categories = CompanyCategory.objects.all()

    # Paginate the list of companies
    pagination_context = paginate_queryset(request, items)

    context = {
        'items': pagination_context['items'], 
        'categories': categories,
        'elided_page_range': pagination_context['elided_page_range']
    }

    return render(request, template, context)


@conditional_cache_page(60 * 60 * 24 * 365, key_prefix="about", condition=not os.getenv("DEBUG"))
def about(request):
    """
    View function for the about page.
    """
    
    template = "website/core/about.html"

    breadcrumbs = [
            {"name": "Home", "url": reverse("website:index")},
            {"name": "About", "url": None},
        ]

    context = {
        "breadcrumbs": breadcrumbs,
    }
    return render(request, template, context)


@conditional_cache_page(60 * 60 * 24 * 365, key_prefix="legal_index", condition=not os.getenv("DEBUG"))
def legal_index(request):
    """
    View function for the legal index page.
    """

    template = "website/legal/legal.html"

    breadcrumbs = [
            {"name": "Home", "url": reverse("website:index")},
            {"name": "Legal", "url": None},
        ]
    
    context = {
        "breadcrumbs": breadcrumbs,
        "website_url": os.getenv("DOMAIN"),
        "website_name": os.getenv("WEBSITE_URL"),
    }
    
    return render(request, template, context)


@conditional_cache_page(60 * 60 * 24 * 365, key_prefix="legal_single", condition=not os.getenv("DEBUG"))
def legal_single(request, slug):
    """
    View function for a single legal detail page.
    """

    template = f"website/legal/{slug.replace('-', '_')}.html"

    breadcrumbs = [
            {"name": "Home", "url": reverse("website:index")},
            {"name": "Legal", "url": reverse("website:legal_index")},
            {"name": " ".join(slug.split("-")).title(), "url": None},
        ]

    context = {
        "breadcrumbs": breadcrumbs,
    }

    return render(request, template, context)


@conditional_cache_page(60 * 60 * 24 * 365, key_prefix="archive", condition=not os.getenv("DEBUG"))
def archive(request):
    """
    View function for the archive page.
    """
    template = "website/core/archive.html"

    breadcrumbs = [
        {"name": "Home", "url": reverse('website:index')},
        {"name": "Archive", "url": None},
    ]

    # Query all categories and companies based on type
    softwares = Company.objects.filter(company_type=1) 

    # Query software categories and exclude categories with empty slugs
    software_categories = CompanyCategory.objects.filter(company__in=softwares).distinct().exclude(slug='')

    context = {
        "breadcrumbs": breadcrumbs,
        "softwares": softwares,
        "software_categories": software_categories,
    }
    
    return render(request, template, context)


def custom_404_view(request, exception=None):
    template = "website/404.html"
    return render(request, template, status=404)


# endregion CORE
# --------------------


# --------------------
# region COMPANY


@conditional_cache_page(60 * 60 * 24 * 365, key_prefix="company_index", condition=not os.getenv("DEBUG"))
def company_index(request):
    """
    View function for the company index page.
    """

    # Define the template to use
    template = "website/company/index.html"

    # Fetch all companies
    company_queryset = Company.objects.all()
    category_queryset = CompanyCategory.objects.all()

    # Paginate the list of companies
    companies = paginate_queryset(request, company_queryset)
    categories = paginate_queryset(request, category_queryset) 

    breadcrumbs = [
        {"name": "Home", "url": reverse("website:index")},
        {"name": "Directory", "url": None},
    ]  

    context = {
        'items': companies,
        'categories': categories,
    }

    return render(request, template, context)


@conditional_cache_page(60 * 60 * 24 * 365, key_prefix="company_single", condition=not os.getenv("DEBUG"))
def company_single(request, slug):
    """
    View function for a single company detail page.
    """
    # Fetch the specific company by the slug
    company = get_object_or_404(Company, slug=slug)
    
    # Define a mapping from company type to template path
    template_paths = {
        1: "website/company/software/single.html",
        2: "website/company/service_provider/single.html",
        3: "website/company/local_business/single.html",
        4: "website/company/merchant_account_provider/single.html",
    }

     # Get the template path based on the company type
    template = template_paths.get(company.company_type)

    context = {
        'item': company,
    }

    return render(request, template, context)


@conditional_cache_page(60 * 60 * 24 * 365, key_prefix="company_collection", condition=not os.getenv("DEBUG"))
def company_collection(request, slug):
    """
    View function for a single company detail page.
    """
    template = "website/company/software/collection.html"

    # Fetch the specific category based on the slug
    category = get_object_or_404(CompanyCategory, slug=slug)

    # Fetch all companies in the category
    companies = Company.objects.filter(categories__name=category.name)

    if not companies.exists():
        raise Http404("No companies found for this category.")


    breadcrumbs = [
        {"name": "Home", "url": reverse("website:index")},
        {"name": "Directory", "url": reverse("website:company_index")},
        {"name": category.name, "url": None},
    ]  

    context = {
        'items': companies,
        'category': category,
        'breadcrumbs': breadcrumbs,
    }

    return render(request, template, context)


# endregion COMPANY
# --------------------


# --------------------
# region TOOLS

@conditional_cache_page(60 * 60 * 24 * 365, key_prefix="tools_index", condition=not os.getenv("DEBUG"))
def tools_index(request):

    # Define the template to use
    template = "website/tools/index.html"

    # Fetch all companies
    # tools_queryset = Tools.objects.all()
    # category_queryset = ToolsCategory.objects.all()

    # Paginate the list of companies
    # tools = paginate_queryset(request, tools_queryset)
    # categories = paginate_queryset(request, category_queryset) 

    breadcrumbs = [
        {"name": "Home", "url": reverse("website:index")},
        {"name": "Tools", "url": None},
    ]  

    context = {
        # 'items': tools,
        # 'categories': categories,
    }

    return render(request, template, context)

@conditional_cache_page(60 * 60 * 24 * 365, key_prefix="tools_single", condition=not os.getenv("DEBUG"))
def tools_single(request, slug):

    # Fetch the specific tool by the slug
    # tool = get_object_or_404(Tool, slug=slug)

    # Get the template path based on the tool type
    template = f"website/tools/single/{slug.replace('-','_')}.html"

    breadcrumbs: [
        {"name": "Home", "url": "/"},
        {"name": "Tools", "url": reverse("website:tools_index")},
        # {"name": "Combine Tools", "url": reverse('website:tools_collection_combine')},
    ]

    context = {
        # 'item': tool,
    }

    return render(request, template, context)


# endregion TOOLS
# --------------------





# ------------------------------
# region HELPER VIEWS


def clear_cache(request):
    password = request.GET.get("password")

    if password != "clearcache":
        return HttpResponse("Unauthorized", status=401)

    cache.clear()
    return HttpResponse("Cache cleared successfully")


# endregion HELPER FUNCTIONS
# ------------------------------
