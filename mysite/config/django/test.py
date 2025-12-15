from .base import *

# Φορτώνει το ίδιο .env.dev ή ξεχωριστό .env.test αν υπάρχει
env.read_env(BASE_DIR / ".env.test", overwrite=True)  # ή ".env.test"

# Επιβάλουμε το WhiteNoise Storage για βελτιστοποίηση:
# (Αυτό αντικαθιστά τυχόν παλιές ρυθμίσεις STORAGES από το base.py)
# STORAGES = {
#     "staticfiles": {
#         "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
#     },
# }

DEBUG = True
SECRET_KEY = env("SECRET_KEY")
ALLOWED_HOSTS = ["*"]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': env("DB_NAME"),  # ξεχωριστή DB για tests
        'USER': env("DB_USER"),
        'PASSWORD': env("DB_PASSWORD"),
        'HOST': env("DB_HOST"),
        'PORT': env("DB_PORT", default='5432'),
    }
}

STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles_test"
STATICFILES_DIRS = [BASE_DIR / "static"]
MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media_test"
