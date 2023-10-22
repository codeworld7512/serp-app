# website/context_processors.py

from django.conf import settings
import os

def global_env_vars(request):
    domain = os.getenv("DOMAIN")
    domain_ = os.getenv("DOMAIN_")
    website_name = os.getenv("WEBSITE_NAME")
    serply_slug = os.getenv("SERPLY_SLUG")
    gtm_tag = os.getenv("GTM_TAG")
    amz_tag = os.getenv("AMZ_TAG")

    return {
        "domain": domain,
        "domain_": domain_,
        "website_name": website_name,
        "serply_slug": serply_slug,
        "gtm_tag": gtm_tag,
        "amz_tag": amz_tag

    }
