"""
Django settings for okthess project.

Generated by 'django-admin startproject' using Django 1.11.3.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os

import raven
from django.utils.translation import ugettext_lazy as _

from okthess import helpers


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
if helpers.is_ec2_linux():
    DEBUG = False

ALLOWED_HOSTS = [
    'localhost',
    '127.0.0.1',
    '.elasticbeanstalk.com',
    '.okthess.gr',
]

# ElasticBeanstalk healthcheck sends requests with host header = internal ip
# So we detect if we are in elastic beanstalk, and add the instances private ip address
private_ip = helpers.get_linux_ec2_private_ip()
if private_ip:
    ALLOWED_HOSTS.append(private_ip)


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY', 'secret')


# Application definition

INSTALLED_APPS = [
    'main.apps.MainConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.redirects',
    's3direct',
    'ckeditor',
]

SITE_ID = 1

if not DEBUG:
    INSTALLED_APPS.append('raven.contrib.django.raven_compat')

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.contrib.redirects.middleware.RedirectFallbackMiddleware',
]

ROOT_URLCONF = 'okthess.urls'

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

WSGI_APPLICATION = 'okthess.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'okthess',
        'USER': 'okthess',
        'PASSWORD': 'okthess',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}

# AWS production
if 'RDS_HOSTNAME' in os.environ:
    # Shame on AWS, ding ding
    hostname = os.environ['RDS_HOSTNAME'].split(':')[0]
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': os.environ['RDS_DB_NAME'],
            'USER': os.environ['RDS_USERNAME'],
            'PASSWORD': os.environ['RDS_PASSWORD'],
            'HOST': hostname,
            'PORT': os.environ['RDS_PORT'],
        }
    }

# TravisCI testing
if 'TRAVIS' in os.environ:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'okthess',
            'USER': 'postgres',
            'PASSWORD': '',
            'HOST': '127.0.0.1',
            'PORT': '5432',
        }
    }


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

LANGUAGES = [
    ('el', _('Greek')),
    ('en', _('English')),
]

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_ROOT = 'static'
STATIC_URL = '/static/'


# Media (user uploaded content)
# https://docs.djangoproject.com/en/1.11/ref/settings/#media-root

MEDIA_ROOT = os.getcwd()
MEDIA_URL = '/uploads/'


# s3direct - AWS S3 admin upload
# https://github.com/bradleyg/django-s3direct

AWS_ACCESS_KEY_ID = os.environ.get('OKTHESS_AWS_ACCESS_KEY_ID', '')
AWS_SECRET_ACCESS_KEY = os.environ.get('OKTHESS_AWS_SECRET_ACCESS_KEY', '')
AWS_STORAGE_BUCKET_NAME = 'okthess-static'
S3DIRECT_REGION = 'eu-central-1'
S3DIRECT_DESTINATIONS = {
    'uploads': {
        'key': 'uploads',
        'allowed': ['image/jpeg', 'image/png'],
        'cache_control': 'max-age=86400',
        'content_disposition': 'inline',
        'content_length_range': (50, 20000000),
    }
}


# Email
# https://docs.djangoproject.com/en/1.11/topics/email/

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = True
EMAIL_HOST = 'email-smtp.eu-west-1.amazonaws.com'
EMAIL_HOST_USER = os.getenv('OKTHESS_AWS_SES_USER', '')
EMAIL_HOST_PASSWORD = os.getenv('OKTHESS_AWS_SES_PASSWORD', '')
EMAIL_PORT = 587
DEFAULT_FROM_EMAIL = 'webmaster@okthess.gr'
CONTACT_TO_EMAIL = 'admin@okthess.gr'


# Security middleware
# https://docs.djangoproject.com/en/1.11/ref/middleware/#module-django.middleware.security

if not DEBUG:
    SECURE_CONTENT_TYPE_NOSNIFF = True
    SECURE_BROWSER_XSS_FILTER = True
    X_FRAME_OPTIONS = 'DENY'

    # FIXME when SSL is live
    # SESSION_COOKIE_SECURE = True
    # CSRF_COOKIE_SECURE = True
    # SECURE_SSL_REDIRECT = True
    # SECURE_HSTS_SECONDS = 0


# Internationalization and Translation
# https://docs.djangoproject.com/en/1.11/topics/i18n

LOCALE_PATHS = [
    'locale',
]


# Sentry
# https://docs.sentry.io/clients/python/integrations/django/

RAVEN_CONFIG = {
    'dsn': os.environ.get('SENTRY_DSN', ''),
}
