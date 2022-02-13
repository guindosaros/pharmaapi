"""
WSGI config for exper_config project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os
import dotenv

from django.core.wsgi import get_wsgi_application

if os.environ.get("ENV") != "PROD":
    if os.environ.get("ENV") == "TEST":
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pharmaapi.test")
    else:
        dotenv.read_dotenv(dotenv=".env")
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pharmaapi.development")
else:
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pharmaapi.production")

application = get_wsgi_application()
