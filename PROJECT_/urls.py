import os
import debug_toolbar

from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    
    path("admin/", admin.site.urls),
    
    path("", include("website.urls", namespace="website")),

] + static(settings.STATIC_URL, document_root=settings.STATIC_URL)

if settings.DEBUG and debug_toolbar:
    urlpatterns.append(path('__debug__/', include(debug_toolbar.urls)))


