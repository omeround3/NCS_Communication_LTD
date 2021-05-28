"""
Django settings for CommunicationLTD project.

Generated by 'django-admin startproject' using Django 3.2.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

import os
import json
import sys
import dj_database_url
from pathlib import Path
from django.contrib.messages import constants as messages
from django.core.management.utils import get_random_secret_key



# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

with open(os.path.join(BASE_DIR, 'CommunicationLTD/pass_req.json')) as f:
    PASS_REQ = json.load(f)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = 'django-insecure-yx4(-8l*zp5@v4a@ik3*q^=9ht@@xz50k1!s8s)79zw-&)qie&'
SECRET_KEY = os.getenv("DJANGO_SECRET_KEY", get_random_secret_key())    # Random secret key

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv("DEBUG", "False") == "True"

ALLOWED_HOSTS = os.getenv("DJANGO_ALLOWED_HOSTS", "127.0.0.1,localhost").split(",")


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Daniel - Added for password history validation #
    'django_password_validators',
    # Daniel - Added for password history validation #
    'django_password_validators.password_history',
    'core',
    'crispy_forms',
]

CRISPY_TEMPLATE_PACK = 'bootstrap4'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'CommunicationLTD.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'CommunicationLTD.wsgi.application'


# Set development mode
DEVELOPMENT_MODE = os.getenv("DEVELOPMENT_MODE", "False") == "True"

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'CommunicationLTD',
        'USER': 'administrator',
        'PASSWORD': 'zX7Yj86L9wMW!',
        'HOST': '51.116.168.249',
        'PORT': '3306'
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django_password_validators.password_character_requirements.password_validation.PasswordCharacterValidator',
        'OPTIONS': {
                'min_length_digit': PASS_REQ["password_content"]["min_length_digit"],
                'min_length_alpha': PASS_REQ["password_content"]["min_length_alpha"],
                'min_length_special': PASS_REQ["password_content"]["min_length_special"],
                'min_length_lower': PASS_REQ["password_content"]["min_length_lower"],
                'min_length_upper': PASS_REQ["password_content"]["min_length_upper"],
                'special_characters': PASS_REQ["password_content"]["special_characters"]
        }
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        'OPTIONS': {
            'min_length': PASS_REQ["min_length"],
        }
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
]

AUTH_PASSWORD_VALIDATORS_2 = [
    {
        'NAME': 'django_password_validators.password_character_requirements.password_validation.PasswordCharacterValidator',
        'OPTIONS': {
                'min_length_digit': PASS_REQ["password_content"]["min_length_digit"],
                'min_length_alpha': PASS_REQ["password_content"]["min_length_alpha"],
                'min_length_special': PASS_REQ["password_content"]["min_length_special"],
                'min_length_lower': PASS_REQ["password_content"]["min_length_lower"],
                'min_length_upper': PASS_REQ["password_content"]["min_length_upper"],
                'special_characters': PASS_REQ["password_content"]["special_characters"]
        }
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        'OPTIONS': {
            'min_length': PASS_REQ["min_length"],
        }
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django_password_validators.password_history.password_validation.UniquePasswordsValidator',
        'OPTIONS': {
            'last_passwords': PASS_REQ["password_history"]  # Only the last 3 passwords entered by the user
        }
    },
]

# Password hashers
# https://docs.djangoproject.com/en/3.2/topics/auth/passwords/
PASSWORD_HASHERS = [
    # Default Haser - Uses PBKDF2 + HMAC + SHA256
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
]

# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Tel_Aviv'

USE_I18N = True

USE_L10N = True

USE_TZ = True

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
# STATICFILES_DIRS = (
#     os.path.join(BASE_DIR, "./core/static"),
# )

# Simplified static file serving.
# https://warehouse.python.org/project/whitenoise/


# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# Messages integrated with Bootstrap
MESSAGE_TAGS = {
    messages.DEBUG: 'alert-secondary',
    messages.INFO: 'alert-info',
    messages.SUCCESS: 'alert-success',
    messages.WARNING: 'alert-warning',
    messages.ERROR: 'alert-danger',
}

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
# SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

