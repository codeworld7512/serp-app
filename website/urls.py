# website/urls.py

from django.urls import path
from website import views
from website.views import custom_404_view

app_name = "website"


urlpatterns = [

    # ----------------------------------
    # region CLEAR CACHE
    
    path("clearcache/", views.clear_cache, name="clear_cache"),

    # endregion CLEAR CACHE
    # ----------------------------------
  

    # ----------------------------------
    # region CORE

    path("", views.index, name="index"),
    # path(f"{settings.GLOBAL_CATEGORY_PREFIX[1:]}", views.category, name="category"),
    path("about/", views.about, name="about"),
    # path("tags/", views.topics, name="topics"),
    path("archive/", views.archive, name="archive"),
    path("legal/", views.legal_index, name="legal_index"),
    path("legal/<slug>/", views.legal_single, name="legal_single"),
    
    # endregion CORE
    # ----------------------------------


    # ----------------------------------
    # region COMPANY
    
    path("directory/", views.company_index, name="company_index"),
    path("reviews/best/<slug:slug>/", views.company_collection, name="company_collection"),
    path("review/<slug>", views.company_single, name="company_single"),

    # endregion COMPANY
    # ----------------------------------


    # ----------------------------------
    # region TOOLS
    
    path("tools/", views.tools_index, name="tools_index"),
    path("tool/<slug>/", views.tools_single, name="tools_single"),

    # endregion TOOLS
    # ----------------------------------


]

handler404 = custom_404_view