"""
Django settings for hyposoft project.

Generated by 'django-admin startproject' using Django 3.0.2.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os
import logging

logging.basicConfig(level=logging.ERROR)

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
from rest_framework.permissions import BasePermission, SAFE_METHODS, IsAdminUser

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '2y9vhvh!y-ono@msw2$l7s9h8ld_edy%9mn%sq22vs47vi=mt)'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

BCMAN_PASSWORD = os.getenv('BCMAN_PASSWORD')

if not BCMAN_PASSWORD: 
    raise Exception('environment variable BCMAN_PASSWORD not set')

ALLOWED_HOSTS = [
    "localhost",
    "hyposoft.tech",
    "dev.bitasy.me",
    "carter.bitasy.me",
    "amber.bitasy.me"
]

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework.authtoken',
    'django_filters',
    'hyposoft',
    'equipment',
    'import_export',
    'frontend',
    'changeplan',
    'system_log',
    'bulk',
    'network',
    'power',
    'hypo_auth',
    'multiselectfield',
]

IMPORT_EXPORT_USE_TRANSACTIONS = True

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'hypo_auth.middleware.ShibbolethRemoteUserMiddleware',
]

ROOT_URLCONF = 'hyposoft.urls'

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

WSGI_APPLICATION = 'hyposoft.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'prod',
        'USER': 'vcm',
        'PASSWORD': 'hyposoft',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'hypo_auth.backends.ShibbolethRemoteUserBackend',
)

SHIBBOLETH_ATTRIBUTE_MAP = {
    "uid": (True, "username"),
    "givenName": (True, "first_name"),
    "sn": (True, "last_name"),
}

SHIB_URL = (
    'https://vcm-13060.vm.duke.edu/Shibboleth.sso'
    if DEBUG else
    'https://hyposoft.tech/Shibboleth.sso'
)

SHIB_LOGIN_URL = SHIB_URL+"/Login"
SHIB_LOGOUT_URL = SHIB_URL+"/Logout"

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.SessionAuthentication'
    ],
    # 'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    # 'PAGE_SIZE': 50,
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend']
}


class ReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS or request.user.is_staff


if not DEBUG:
    REST_FRAMEWORK['DEFAULT_PERMISSION_CLASSES'] = [
        'hyposoft.settings.ReadOnly'
    ]

# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

MEDIA_ROOT = os.path.join(BASE_DIR, "media/")
STATIC_ROOT = os.path.join(BASE_DIR, "static/")
STATIC_URL = '/static/'

LOGOUT_REDIRECT_URL = "/"
