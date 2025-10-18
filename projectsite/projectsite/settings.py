"""
Django settings for projectsite project.
"""

import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
SECRET_KEY = 'django-insecure-your-secret-key-here'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['cornick.pythonanywhere.com', '127.0.0.1', 'localhost']

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',  # Required for allauth
    
    # Your apps
    'tasks',
    'pwa',  # PWA app

    # AllAuth apps
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    
    # Social providers
    'allauth.socialaccount.providers.google',
    'allauth.socialaccount.providers.github',
]

SITE_ID = 1

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'allauth.account.middleware.AccountMiddleware',
]

ROOT_URLCONF = 'projectsite.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

WSGI_APPLICATION = 'projectsite.wsgi.application'

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validation
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
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
STATIC_ROOT = BASE_DIR / 'staticfiles'

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# AllAuth Settings
LOGIN_REDIRECT_URL = '/'  # Redirect to home after login
ACCOUNT_LOGOUT_REDIRECT_URL = '/accounts/login/'  # Redirect to login after logout
LOGIN_URL = '/accounts/login/'  # Where to redirect for login

# Updated Account configuration (using new settings)
ACCOUNT_LOGIN_METHODS = {'email', 'username'}  # Login with username or email
ACCOUNT_SIGNUP_FIELDS = ['email*', 'username*', 'password1*', 'password2*']  # Signup fields with validation

# DISABLE EMAIL VERIFICATION - FIX FOR CONNECTION ERROR
ACCOUNT_EMAIL_VERIFICATION = 'none'  # Changed from 'optional' to 'none'
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'  # Add this line

# Session settings
ACCOUNT_LOGOUT_ON_GET = False  # Change this to False for security
ACCOUNT_SESSION_REMEMBER = True  # Remember login sessions

# Social account specific
SOCIALACCOUNT_AUTO_SIGNUP = True  # Automatically sign up social users
SOCIALACCOUNT_EMAIL_VERIFICATION = 'none'  # Changed from 'optional' to 'none'
SOCIALACCOUNT_EMAIL_REQUIRED = False  # Changed from True to False

# Social Account Providers
SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'SCOPE': [
            'profile',
            'email',
        ],
        'AUTH_PARAMS': {
            'access_type': 'online',
        },
        'APP': {
            'client_id': os.getenv('GOOGLE_CLIENT_ID', ''),
            'secret': os.getenv('GOOGLE_CLIENT_SECRET', ''),
            'key': ''
        }
    },
    'github': {
        'SCOPE': [
            'user',
            'email',
        ],
        'APP': {
            'client_id': os.getenv('GITHUB_CLIENT_ID', ''),
            'secret': os.getenv('GITHUB_CLIENT_SECRET', ''),
            'key': ''
        }
    }
}

# --- Progressive Web App Settings ---
PWA_APP_NAME = 'ProjectSite'
PWA_APP_DESCRIPTION = "A Progressive Web App version of ProjectSite"
PWA_APP_THEME_COLOR = '#0A0A0A'
PWA_APP_BACKGROUND_COLOR = '#FFFFFF'
PWA_APP_DISPLAY = 'standalone'
PWA_APP_SCOPE = '/'
PWA_APP_ORIENTATION = 'portrait'
PWA_APP_START_URL = '/'
PWA_APP_STATUS_BAR_COLOR = 'default'
PWA_APP_ICONS = [
    {
        'src': '/static/images/icon-192.png',
        'sizes': '192x192'
    },
    {
        'src': '/static/images/icon-512.png',
        'sizes': '512x512'
    }
]
PWA_APP_ICONS_APPLE = [
    {
        'src': '/static/images/icon-192.png',
        'sizes': '192x192'
    },
    {
        'src': '/static/images/icon-512.png',
        'sizes': '512x512'
    }
]
PWA_APP_DIR = 'ltr'
PWA_SERVICE_WORKER_PATH = os.path.join(BASE_DIR, 'static', 'js', 'serviceworker.js')