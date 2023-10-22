# PROJECT_/settings/production.py

import os

import sentry_sdk
from .settings import *



sentry_sdk.init(
    dsn=os.getenv("SENTRY_DSN"),
    send_default_pii=True,
    traces_sample_rate=1.0,
    profiles_sample_rate=1.0,
)

DEBUG = os.getenv('DEBUG', default=False)

CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': os.getenv("REDIS_URL"),
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
        }
    }
}