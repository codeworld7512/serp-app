# PROJECT_/settings/development.py

from .settings import *


SECRET_KEY = "development"

ALLOWED_HOSTS = []

DEBUG = True

INTERNAL_IPS = [
    '127.0.0.1',
    'localhost',
]

INSTALLED_APPS += [
    "debug_toolbar",
    "import_export",
]

MIDDLEWARE += [
    "debug_toolbar.middleware.DebugToolbarMiddleware",
]

