import django_heroku
from .base import *


DEBUG = False

# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.postgresql_psycopg2",
#         "NAME": os.environ.get("DATABASE_NAME"),
#         "USER": os.environ.get("DATABASE_USER"),
#         "PASSWORD": os.environ.get("DATABASE_PASS"),
#         "HOST": os.environ.get("DATABASE_HOST"),
#         "PORT": os.environ.get("SECRET_PORT"),
#     }
# }

# SECURITY WARNING: don't run with debug turned on in production!
ALLOWED_HOSTS = ["*", "medoc-api.herokuapp.com"]


STATIC_URL = "/static/"

STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"


django_heroku.settings(locals())
