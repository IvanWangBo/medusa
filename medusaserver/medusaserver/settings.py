# coding:utf-8

"""
Django settings for medusaserver project.

Generated by 'django-admin startproject' using Django 1.8.14.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'e^s16tdqiuewo716@@lpyql!br!w=vaki*ki849xh_c6&cm2_4'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # ------------------------------
    # Django Debug Toolbar
    'debug_toolbar',
    # django-celery
    'djcelery',
    # Django REST framework
    'rest_framework',
    # Sentry Raven
    'raven.contrib.django.raven_compat',
    # ------------------------------
    'myapp',
    'rest',
    'tasks',
    # ------------------------------
)

MIDDLEWARE_CLASSES = (
    # ------------------------------
    # Sentry Raven
    'raven.contrib.django.raven_compat.middleware.Sentry404CatchMiddleware',
    # ------------------------------
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'medusaserver.urls'


# DjangoTemplates
TEMPLATES_DJANGO = [
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

# Jinja2
TEMPLATES_JINJA2 = [
    {
        'BACKEND': 'django.template.backends.jinja2.Jinja2',
        'DIRS': [],
        # When APP_DIRS is True, Jinja2 engines look for templates
        # in the jinja2 subdirectory of installed applications.
        'APP_DIRS': True,
        'OPTIONS': {
            # The default configuration is purposefully kept to a minimum.
            # The Jinja2 backend doesn’t create a Django-flavored environment.
            # It doesn’t know about Django context processors, filters, and tags.
            # In order to use Django-specific APIs, you must configure them into the environment.
            'environment': 'medusaserver.jinja2.environment',
        },
    },
]


WSGI_APPLICATION = 'medusaserver.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

# TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
STATIC_ROOT = '/home/workspace/static/'

# URL prefix for static files.
STATIC_URL = '/static/'

# This setting defines the additional locations the staticfiles app will traverse
# if the FileSystemFinder finder is enabled.
STATICFILES_DIRS = [
    '/home/workspace/medusa/medusaserver/static',
]

# ====================================================================================================
# MySQL
DATABASES_MYSQL = {
    'default': {
        # django.db.backends.mysql
        'ENGINE': 'django.db.backends.mysql',
        # my own mysql
        # 'ENGINE': 'lib.mysql',
        'NAME': 'medusa',
        'USER': 'medusa',
        'PASSWORD': 'medusa',
        'HOST': '192.168.100.100',
        'PORT': '3306',
    }
}

# PostgreSQL
DATABASES_POSTGRESQL = {
    'default': {
        # django.db.backends.postgresql_psycopg2
        # 'ENGINE': 'django.db.backends.postgresql_psycopg2',
        # my own postgresql_psycopg2
        'ENGINE': 'lib.postgresql_psycopg2',
        # CONN_MAX_AGE:
        # The lifetime of a database connection, in seconds.
        # Use 0 to close database connections at the end of each request — Django’s historical behavior
        # Use None for unlimited persistent connections.
        'CONN_MAX_AGE': None,
        'NAME': 'medusa',
        'USER': 'medusa',
        'PASSWORD': 'medusa@psql',
        'HOST': '192.168.100.100',
        'PORT': '5432',
    }
}


CACHES = {
    'default': {
        'BACKEND': 'redis_cache.RedisCache',
        'LOCATION': 'redis://192.168.100.100:6379',
        'OPTIONS': {
            'DB': 1,
        },
    }
}

TIME_ZONE = 'Asia/Shanghai'

# LOGGING = {
#     'version': 1,
#     'disable_existing_loggers': False,
#     'handlers': {
#         'mail_admins': {
#             'level': 'ERROR',
#             'class': 'django.utils.log.AdminEmailHandler'
#         }
#     },
#     'loggers': {
#         'django.request': {
#             'handlers': ['mail_admins'],
#             'level': 'ERROR',
#             'propagate': True,
#         },
#     }
# }

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
    },
    'handlers': {
        'sentry': {
            'level': 'ERROR', # To capture more than ERROR, change to WARNING, INFO, etc.
            'class': 'raven.contrib.django.raven_compat.handlers.SentryHandler',
            'formatter': 'verbose',
            'tags': {'custom-tag': 'x'},
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        }
    },
    'loggers': {
        'root': {
            'level': 'WARNING',
            'handlers': ['sentry'],
        },
        'django.db.backends': {
            'level': 'ERROR',
            'handlers': ['console'],
            'propagate': False,
        },
        'raven': {
            'level': 'DEBUG',
            'handlers': ['console'],
            'propagate': False,
        },
        'sentry.errors': {
            'level': 'DEBUG',
            'handlers': ['console'],
            'propagate': False,
        },
    },
}

# ====================================================================================================
# Configure Django project to use Celery

# [1] RabbitMQ as broker
BROKER_URL = 'amqp://celery_user:celery_password@192.168.100.100:5672/celery_vhost'

# [2] redis as broker
# BROKER_URL = 'redis://192.168.100.100:6379/0'

# result_backend
CELERY_RESULT_BACKEND = 'redis://192.168.100.100:6379/2'

import djcelery
djcelery.setup_loader()
# ====================================================================================================
# Django REST framework

REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        # 'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly',
        'rest_framework.permissions.IsAdminUser',
    ],
    'PAGE_SIZE': 10,
}
# ====================================================================================================
# Sentry Raven

import raven
RAVEN_CONFIG = {
    'dsn': 'http://a5b24f6c7bf54fea9078a66e1ac14ab4:d2225864d4b3459c89a329454cea4c1e@192.168.100.100:9000/2',
    # If you are using git, you can also automatically configure the release based on the git info.
    # 'release': raven.fetch_git_sha(os.path.dirname(__file__)),
}
# ====================================================================================================
TEMPLATES = TEMPLATES_DJANGO
# TEMPLATES = TEMPLATES_JINJA2

# DATABASES = DATABASES_MYSQL
DATABASES = DATABASES_POSTGRESQL
# ====================================================================================================
