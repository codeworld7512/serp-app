# website/admin.py

from django.contrib import admin
# admin.py
from import_export.admin import ImportExportModelAdmin
from .resources import CompanyResource, CompanyCategoryResource
from django.contrib.admin import TabularInline

from .models import (
    Company,
    CompanyCategory,
    Feature,
    Pricing
)


# ------------------------------------
# region ADMIN ACTIONS

def set_has_affiliate_program_true(modeladmin, request, queryset):
    queryset.update(has_affiliate_program=True)
set_has_affiliate_program_true.short_description = "Set has_affiliate_program to True"

def set_has_affiliate_program_unknown(modeladmin, request, queryset):
    queryset.update(has_affiliate_program=None)
set_has_affiliate_program_unknown.short_description = "Set has_affiliate_program to Unknown"

# endregion ADMIN ACTIONS
# --------------------------------



# ------------------------------------
# region ADMIN REGISTRATION



class CompanyInline(admin.TabularInline):
    model = Company.alternatives.through  
    fk_name = 'from_company'  
    extra = 1


@admin.register(Company)
class CompanyAdmin(ImportExportModelAdmin):
    inlines = [CompanyInline]
    resource_class = CompanyResource
    search_fields = ('name', 'slug')
    list_display = ('name', 'slug', 'one_liner', 'display_alternatives')
    # list_editable = ('display_alternatives',)
    ordering = ('-created_at',)
    actions = [set_has_affiliate_program_true, set_has_affiliate_program_unknown]
    filter_horizontal = ('categories',)

    def display_alternatives(self, obj):
        """Returns a comma-separated list of alternative companies' names."""
        return ", ".join([alt.name for alt in obj.alternatives.all()])
    display_alternatives.short_description = 'Alternatives'



class CompanyCategoryInline(admin.TabularInline):
    model = Company.categories.through  
    fk_name = 'company'  
    extra = 1

@admin.register(CompanyCategory)
class CompanyCategoryAdmin(ImportExportModelAdmin):
    resource_class = CompanyCategoryResource
    list_display = ('name', 'slug')
    search_fields = ('name', 'slug')
    ordering = ('name',)
    


@admin.register(Feature)
class FeatureAdmin(admin.ModelAdmin):
    list_display = ('feature', 'company')
    search_fields = ('feature', 'company_name')
    list_filter = ('company',)
    ordering = ('feature',)


@admin.register(Pricing)
class PricingAdmin(admin.ModelAdmin):
    list_display = ('company', 'price', 'pricing_model')
    search_fields = ('company__name', 'pricing_model')
    list_filter = ('pricing_model', 'has_free_plan', 'has_free_trial', 'is_open_source') 
    ordering = ('company',)



# endregion ADMIN REGISTRATION
# ------------------------------------