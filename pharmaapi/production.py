from .base import *

DEBUG = False

# SECURITY WARNING: don't run with debug turned on in production!
ALLOWED_HOSTS = ["*"]


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


STATIC_URL = "/static/"

STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")

# Media files config
MEDIA_URL = "/media/"  # or any prefix you choose
MEDIA_ROOT = os.path.join(BASE_DIR, "media")
