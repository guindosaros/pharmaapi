import django_heroku
from .base import *


DEBUG = False

# SECURITY WARNING: don't run with debug turned on in production!
ALLOWED_HOSTS = ["medoc-api.herokuapp.com"]


STATIC_URL = "/static/"

STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")

# Media files config
MEDIA_URL = "/media/"  # or any prefix you choose
MEDIA_ROOT = os.path.join(BASE_DIR, "media")


django_heroku.settings(locals())
