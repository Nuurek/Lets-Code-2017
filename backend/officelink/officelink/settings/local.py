from .base import *
import os

ALLOWED_HOSTS += (
    '127.0.0.1',
    'localhost',
)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'officelink',
        'USER': 'officelink',
        'PASSWORD': 'potter123',
        'HOST': 'localhost',
        'PORT': '',
    }
}