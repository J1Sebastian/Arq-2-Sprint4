"""
Django settings for monitoring project.

Generated by 'django-admin startproject' using Django 3.2.6.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-5r69%z1q=&+c6u@i1#izdtqhcgc4wzu=b1un3l9_parfoaqapp'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'usuarios',
    'social_django',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


ROOT_URLCONF = 'monitoring.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'usuarios', 'templates', 'usuarios')],
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

WSGI_APPLICATION = 'monitoring.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': "usuarios_db", 
        "USER": "usuarios_user", 
        "PASSWORD": "isis2503",
        "HOST": "10.128.0.7",  # IP privada de la base de datos del ms
        "PORT": "5432",  # 5432
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
STATIC_ROOT = os.path.join(PROJECT_ROOT, 'staticfiles')

STATIC_URL = '/static/'
MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'media')
MEDIA_URL = '/media/'

# Extra places for collectstatic to find static files.
STATICFILES_DIRS = (
    os.path.join(PROJECT_ROOT, 'static'),
)

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Authentication

LOGIN_URL = "/login/auth0" 
LOGIN_REDIRECT_URL = "/" 
LOGOUT_REDIRECT_URL = "https://widmy-lasdivinas.us.auth0.com/v2/logout?returnTo=http%3A%2F%2F34.170.215.124:8080"
SOCIAL_AUTH_TRAILING_SLASH = False # Remove end slash from routes 
SOCIAL_AUTH_AUTH0_DOMAIN = 'widmy-lasdivinas.us.auth0.com' 
SOCIAL_AUTH_AUTH0_KEY = 'Yv1aZUTFAXqG2MJo8RgflOzU0oSSyYCK' 
SOCIAL_AUTH_AUTH0_SECRET = 'fue-pI5xdn0Ayh8aQPkeNrwu_7sKRPXprPhJ5KBeG9DLDWOZVsm6-9ACmiZcx3b2' 
SOCIAL_AUTH_AUTH0_SCOPE = [ 'openid', 'profile', 'email', 'role', ] 
AUTHENTICATION_BACKENDS = { 'autenticador.auth0backend.Auth0', 'django.contrib.auth.backends.ModelBackend', }

# Microservices: TODO

PATH_PACIENTES = "http://IP_PRIVADA_MS:8080/pacientes"
PATH_EPS = "http://IP_PRIVADA_MS:8080/epss"
PATH_USUARIOS = "http://IP_PRIVADA_MS:8080/usuarios"
