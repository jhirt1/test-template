import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

DEBUG = True

ALLOWED_HOSTS = ['*']

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')