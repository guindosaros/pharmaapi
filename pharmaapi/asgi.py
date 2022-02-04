"""
ASGI config for exper_config project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

import os
import dotenv

from django.core.asgi import get_asgi_application

if os.environ.get("ENV") != "PROD":
    dotenv.read_dotenv()
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pharmaapi.development")
else:
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pharmaapi.production")

application = get_asgi_application()
